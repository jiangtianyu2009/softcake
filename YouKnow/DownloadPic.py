import os
import re
import shutil
import urllib.request

import bs4
import requests

base_url = 'http://www.p42u.com/cn/vl_searchbyid.php?keyword='
filterWord = "video_jacket_img"
srcDirList = [r'Y:\TCNEW', r'G:\tempg\TC']

for srcDir in srcDirList:
    filenames = os.listdir(srcDir)
    for filename in filenames:
        preFileName = filename.split(".")[0]
        if preFileName[-1] == "A" or preFileName[-1] == "B" or preFileName[-1] == "C":
            preFileName = preFileName[0:len(preFileName) - 1]
        destPicName = srcDir + os.sep + preFileName + '.jpg'
        if os.path.isfile(destPicName):
            print(destPicName + ' already here.\n')
        else:
            full_url = base_url + preFileName
            response = requests.get(full_url)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            try:
                imgsrc = 'http:' + soup.find(id=filterWord)['src']
                print(preFileName + "\n" + imgsrc)
                print(destPicName + "\n")
                if not os.path.isfile(destPicName):
                    urllib.request.urlretrieve(imgsrc, destPicName)
            except:
                print('!!!!!!!!!!!!!! Can not find picture of ' + filename + '\n')
