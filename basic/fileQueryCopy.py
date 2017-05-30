# the method moves items from a source to a target, using a filter as the third variable

import os
import shutil
import fnmatch

def fileList(source, target, query):
    matches = []
    for root, dirs, files in os.walk(source):
        for name in files:
            if fnmatch.fnmatch(name, query):
                filePath = os.path.join(root, name)
                os.makedirs(target + os.path.dirname(filePath[len(source):]), exist_ok=True)
                shutil.copy2(filePath, target + filePath[len(source):])
                matches.append(filePath)
    return matches

fileList('/Users/user/Documents/Privat/test', '/Users/user/Documents/Privat/new', 'OS*_Cover*.jpg')
