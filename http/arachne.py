import json
import requests
import csv
import os

example = 'D-DAI-DAM-HP-f-K13-U024-006_SYRHER.tif'
pathName = 'list.csv'

api_token = 'Basic ###'
api_url_base = 'https://arachne.dainst.org/data/'

headers = {'Content-Type': 'application/json',
           'Authorization': api_token}

def getArachneId(term):

    response = requests.get(api_url_base + 'search?q=' + term, headers=headers)

    if response.status_code == 200:
        res = response.json()
        return res['entities'][0]['entityId']
    else:
        return None

def getPathById(entityId):

    response = requests.get(api_url_base + 'entity/' + str(entityId), headers=headers)

    if response.status_code == 200:
        res = response.json()
        return res['editorSection']['content'][0]['value']
    else:
        return None


file = open(os.path.join(pathName), "rU")
reader = csv.reader(file, delimiter=',')

resultList = []
for row in reader:
    term = row[0]
    term = 'Bestand-' + term.replace('.tif','.JPG')
    entityId = getArachneId(term)
    path = getPathById(entityId)
    result = [row[0], entityId, path]
    resultList.append(result)

print(resultList)

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(resultList)
