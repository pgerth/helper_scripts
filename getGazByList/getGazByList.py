import json
import requests
import csv

def getGazById(gazId):
    r = requests.get('https://gazetteer.dainst.org/place/' + str(gazId) + '.json')
    data = r.json()
    try:
        print(data['prefLocation']['coordinates'])
    except KeyError as e:
        print(e)
    return

with open('places.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        getGazById(row[0])
