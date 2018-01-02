# author: Philipp Gerth
#
# The intention of the script is to enrich a csv with gazetteer Ids
# (https://gazetteer.dainst.org/) by coordinates.
#
# Parameters:
# -i --input= This parameter hands over the input file name of the csv
# -c --column= This parameter hands over the column number of the gazetteer Id,
#  numbering starts with 0!
# -d --delimiter= This optional parameter is used to define the delimiter of
#  the input csv file, per default ";" is used!
#
# Examples:
#
# python getGazByList.py -c 'relative/path/places.csv' -c 0 -d ,
# python getGazByList.py -c 'relative/path/synode.csv' -c 3

import sys, getopt
import json
import requests
import csv

inputFile=""
outputFile=""
gazColumn=""
csvDelim=";"

def getGazById(gazId):
    try:
        r = requests.get('https://gazetteer.dainst.org/place/' + str(gazId) + '.json')
        data = r.json()
    except json.decoder.JSONDecodeError:
        print("Gazetteer entry missing for: " + gazId + ". Perhaps wrong Id?")
        return

    try:
        return data['prefLocation']['coordinates']
    except KeyError:
        return

def createOutputFile():
    print(inputFile)
    iFile = open(inputFile, 'rt')
    reader = csv.reader(iFile, delimiter=csvDelim)

    outputFilename = inputFile.strip('.csv') + '_gaz' + '.csv'
    oFile = open(outputFilename, 'wt')
    writer = csv.writer(oFile, delimiter=csvDelim)

    for row in reader:
        if row[int(gazColumn)] is not "" or None:
            gazCoords = getGazById(row[int(gazColumn)])
            if gazCoords is not None:
                row.append(gazCoords[0])
                row.append(gazCoords[1])
                writer.writerow(row)

def main(argv):
    global inputFile
    global gazColumn
    global csvDelim

    try:
        opts, args = getopt.getopt(argv,"hi:c:d:",["input=","column=","delimiter="])
    except getopt.GetoptError:
        print('getGazByList.py -i <inputFile> -c <column> [-d <delimiter>]')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('getGazByList.py -i <input> -c <column> [-d <delimiter>]')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputFile = arg
        elif opt in ("-c", "--column"):
            gazColumn = arg
        elif opt in ("-d", "--delimiter"):
            csvDelim = arg

    if inputFile != "":
        print('Csv input file is: ', inputFile)
        createOutputFile()

if __name__ == "__main__":
    main(sys.argv[1:])
