import json
import requests
import csv

gazList=[]

def getGazById(gazId):
    r = requests.get('https://gazetteer.dainst.org/place/' + str(gazId) + '.json')
    data = r.json()
    gazIdXY = [gazId]
    try:
        gazIdXY.extend(data['prefLocation']['coordinates'])
        gazList.append(gazIdXY)
    except KeyError:
        return
    return

with open('places.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row is not None:
            print(row)
            getGazById(row[0])

with open('gazList.csv', 'wt') as exportFile:
    wr = csv.writer(exportFile)
    for row in gazList:
        wr.writerow(row)
