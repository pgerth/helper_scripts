import json
import requests

gazId = 2086499
r = requests.get('https://gazetteer.dainst.org/place/' + str(gazId) + '.json')
data = r.json()
print(data.get('gazId'))
