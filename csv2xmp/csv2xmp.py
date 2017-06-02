# author: Philipp Gerth
#
# The script could be run by handing over a sql statement or a csv file, which
# was prior exported from arachne.
#
# Parameters:
# -c --csvfile= This parameter hands over the location of a csv file containing
#  the extracted arachne image metadata
# -s --sqlquery= This parameter hands over the location of a csv file containing
#  the extracted arachne image metadata
# -t --targetdirectory= This optional parameter is used to define the target
#  directory, if it is in another location
#
# Examples:
#
# python arachne2xmp.py -c 'relative/path/shap-hp.csv' -t 'shap-hp/'
# python arachne2xmp.py --csvfile '/full/path/to/file/csvfile.csv'
# python arachne2xmp.py -s 'SELECT * FROM marbilderinventar JOIN marbilderbestand ON marbilderinventar.DateinameMarbilderinventar = marbilderbestand.DateinameMarbilderbestand LIMIT 5;'

import mapping
import libxmp
import sys, getopt
import csv
import os
from libxmp.consts import XMP_NS_DC as dc
from libxmp.consts import XMP_NS_Photoshop as photoshop
from libxmp.consts import XMP_NS_IPTCCore as Iptc4xmpCore

def metadataToFile(result, targetDir):
    for row in result:
        path = row['SOFSPfad'].replace('https://sofsdav.uni-koeln.de/daicloud06/dai-orientabteilung-damaskus/dai-orientabteilung-damaskus-fotothek/eingelesen_arachne/',targetDir)
        print("------------------------------")
        print(path)
        xmpfile = libxmp.XMPFiles( file_path=path, open_forupdate=True )
        xmp = xmpfile.get_xmp()

        # Edit the xmp attributes of the image
        for key, value in mapping.mapping.items():
            if row[key] != "":
                value = value.strip().split(':', 1)
                xmp.set_property(eval(value[0]), unicode(value[1], 'utf-8'), unicode(row[key], 'utf-8') )

        # Save xmp metadata to the file
        xmpfile.put_xmp(xmp)
        xmpfile.close_file()

def metadataByCsv(file, targetDir):

    with open(file) as csvfile:
        result = csv.DictReader(csvfile, delimiter=',')

        metadataToFile(result, targetDir)

def createFileDict(targetDir, fileType, fileDict):

    for root, dirs, files in os.walk(targetDir, topdown=False):
        for name in files:
            if fileType in name:
                fileDict[name] = os.path.join(root, name)

    return fileDict

def main(argv):
    csvFile = ''
    targetDir = ''
    fileType = ''
    fileDict = {}

    try:
        opts, args = getopt.getopt(argv,"hc:d:t:",["csvfile=","targetdirectory=","filetype="])
    except getopt.GetoptError:
        print 'csv2xmp.py -c <csvfile> -d <targetdirectory> [-t <filetype>]'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'csv2xmp.py -c <csvfile> -d <targetdirectory> [-t <filetype>]'
            sys.exit()
        elif opt in ("-c", "--csvfile"):
            csvFile = arg
        elif opt in ("-d", "--targetdirectory"):
            targetDir = arg
        elif opt in ("-t", "--filetype"):
            fileType = arg

    if csvFile != "":
        print 'Csv input file is: ', csvFile
        createFileDict(targetDir, fileType, fileDict)
        #metadataByCsv(csvFile, targetDir)

if __name__ == "__main__":
    main(sys.argv[1:])
