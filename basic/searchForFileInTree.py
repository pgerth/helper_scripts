# the method moves items from a source to a target, using a filter as the third variable

import os
import shutil
import fnmatch
import sys, getopt

def fileList(source, target, query):
    matches = []
    for root, dirs, files in os.walk(source):
        for name in files:
            if fnmatch.fnmatch(name,query):
                filePath = os.path.join(root, name)
                os.makedirs(target + os.path.dirname(filePath[len(source):]), exist_ok=True)
                shutil.copy2(filePath, target + filePath[len(source):])
                matches.append(filePath)
    return matches

def fileDelete(source, query):
    matches = []
    for root, dirs, files in os.walk(source):
        for name in files:
            if fnmatch.fnmatch(name,query):
                filePath = os.path.join(root, name)
                os.remove(filePath)
                matches.append(filePath)
    return matches

# main function, which takes also care of the parameter handling
def main(argv):
    source =
    target =
    docs = 'searchForFileInTree.py -f <file> -d <directory>'
    try:
        opts, args = getopt.getopt(argv,"hs:t:",["file=","directory="])
    except getopt.GetoptError:
        print docs
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print docs
            sys.exit()
        elif opt in ("-f", "--file"):
            source = arg
        elif opt in ("-d", "--directory"):
            target = arg

if __name__ == "__main__":
    main(sys.argv[1:])
