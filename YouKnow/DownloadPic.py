import os
import re
import shutil
import urllib.request

import bs4
import requests

base_url = 'https://avmask.com/cn/search/'
srcDirList = [r'G:\tempg\TC']

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
            print(full_url)
            response = requests.get(full_url)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            try:
                imgsrc = soup.find('img')['src'].replace('ps.jpg', 'pl.jpg')
                print(imgsrc)
                print(destPicName)
                if not os.path.isfile(destPicName):
                    opener = urllib.request.build_opener()
                    opener.addheaders = [
                        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(imgsrc, destPicName)
            except Exception as err:
                print(err)
                print('!!!!!!!!!!!!!! Can not find picture of ' + filename + '\n')
