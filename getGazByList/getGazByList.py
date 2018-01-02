# small helper script to extract gazetteer information for a given
# list of gaz ids

import sys, getopt
import json
import requests
import csv

csvFile=""
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


def openFile():

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

def main(argv):

    try:
        opts, args = getopt.getopt(argv,"hc:",["csvfile="])
    except getopt.GetoptError:
        print('getGazByList.py -c <csvfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('csv2xmp.py -c <csvfile> -d <targetdirectory> [-t <filetype>]')
            sys.exit()
        elif opt in ("-c", "--csvfile"):
            csvFile = arg

    if csvFile != "":
        print('Csv input file is: ', csvFile)
        openFile()

if __name__ == "__main__":
    main(sys.argv[1:])
