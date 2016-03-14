# the method moves items from a source to a target, using a filter as the third variable

import os
import shutil
import fnmatch

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

# fileList('/Users/phg/Documents/Privat/test', '/Users/phg/Documents/Privat/new', '*.jpg')

# fileDelete('/Users/phg/Documents/Privat/test','*.jpg')


