# getGazByList

The intention of the script is to enrich a csv with gazetteer Ids
(https://gazetteer.dainst.org/) by coordinates.

## Parameters:
-i --input= This parameter hands over the input file name of the csv
-c --column= This parameter hands over the column number of the gazetteer Id,
 numbering starts with 0!
-d --delimiter= This optional parameter is used to define the delimiter of
 the input csv file, per default ";" is used!

## Examples:

python getGazByList.py -c 'relative/path/places.csv' -c 0 -d ,
python getGazByList.py -c 'relative/path/synode.csv' -c 3
