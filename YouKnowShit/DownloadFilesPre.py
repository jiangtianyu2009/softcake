import requests
import bs4
import os
import urllib.request
import shutil
import re

srcDownloadDir = 'G:\\game\\temp'
distDir = 'G:\\game\\temp1'

filenames = os.listdir(srcDownloadDir)
nodirfilenames = os.listdir(srcDownloadDir)
dirnames = []
dirnamestomoves = []
for filename in filenames:
    if (filename.find('.') < 0):
        nodirfilenames.remove(filename)
        dirnames.append(filename)
        dirnamestomoves.append(filename)
    elif (filename.find('.torrent') > 0 or filename.find('.bt.td') > 0):
        nodirfilenames.remove(filename)

print(nodirfilenames)
for nodirfilename in nodirfilenames:
    shutil.move(srcDownloadDir + os.sep + nodirfilename, distDir)
    print('Moving ' + nodirfilename + ' from '
          + srcDownloadDir + os.sep + nodirfilename,
          ' to directory ' + distDir)

print(dirnames)
print(dirnamestomoves)

for dirname in dirnames:
    subfilenames = os.listdir(srcDownloadDir + '\\' + dirname)
    print(subfilenames)
    for subfilename in subfilenames:
        if (subfilename.find('.bt.td') > 0):
            print(dirname + ' cannot move')
            dirnamestomoves.remove(dirname)
    print('------------------------------------------------------------------------------------------------')
print(dirnames)
print(dirnamestomoves)
print('***********************')
for dirnamestomove in dirnamestomoves:
    subtomovefilenames = os.listdir(srcDownloadDir + '\\' + dirnamestomove)
    print(subtomovefilenames)
    for subtomovefilename in subtomovefilenames:
        if (subtomovefilename.find('.torrent') < 0):
            print(subtomovefilename + ' is ready to move')
            shutil.move(srcDownloadDir + os.sep + dirnamestomove +
                        os.sep + subtomovefilename, distDir)
            print('Moving ' + subtomovefilename + ' from '
                  + srcDownloadDir + os.sep + dirnamestomove + os.sep + subtomovefilename,
                  ' to directory ' + distDir)
    print('------------------------------------------------------------------------------------------------')
