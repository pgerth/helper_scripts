# small helper script to extract gazetteer information for a given
# list of gaz ids

import sys, getopt
import json
import requests
import csv

inputFile=""

def getGazById(gazId):
    r = requests.get('https://gazetteer.dainst.org/place/' + str(gazId) + '.json')
    data = r.json()
    try:
        return data['prefLocation']['coordinates']
    except KeyError:
        return

def openFile():
    print(inputFile)
    iFile = open(inputFile, 'rt')
    reader = csv.reader(iFile)

    oFile = open('output.csv', 'wt')
    writer = csv.writer(oFile)

    for row in reader:
        if row is not None:
            print("----")
            print(row[0])
            gazCoords = getGazById(row[0])
            if gazCoords is not None:
                row.append(gazCoords[0])
                row.append(gazCoords[1])
                writer.writerow(row)

    # with open('gazList.csv', 'wt') as exportFile:
    #     wr = csv.writer(exportFile)
    #     for row in gazList:
    #         wr.writerow(row)

def main(argv):
    global inputFile

    try:
        opts, args = getopt.getopt(argv,"hi:",["inputFile="])
    except getopt.GetoptError:
        print('getGazByList.py -i <inputFile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('csv2xmp.py -i <inputFile>')
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            inputFile = arg

    if inputFile != "":
        print('Csv input file is: ', inputFile)
        openFile()

if __name__ == "__main__":
    main(sys.argv[1:])
