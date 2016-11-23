import requests
import bs4
import os
import urllib.request
import shutil
import re


distDir = 'F:\\utorrent\\WEST'
p = re.compile(r'(\D+\d+)\w*(.\w+)')


filenames = os.listdir(distDir)
upperfilenames = []
print(filenames)
for filenamepref in filenames:
    if (filenamepref.find('_') > 0):
        filenameprefit = filenamepref[filenamepref.index('_'):]
    else:
        filenameprefit = filenamepref
    filenamepost = filenameprefit.replace('-', '').replace('_', '')\
        .replace(' ', '').replace('.1080p', '').replace('.720p', '')
    distname = p.search(filenamepost).group(1).upper() + p.search(filenamepost).group(2).lower()
    print(distname)
    os.rename(distDir + os.sep + filenamepref, distDir + os.sep + distname)