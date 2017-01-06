import requests
import bs4
import os
import urllib.request
import shutil
import re

base_url = 'http://www.jav11b.com/cn/vl_searchbyid.php?keyword='
srcDir = r'E:\download\TC'
filterWord = "video_jacket_img"

filenames = os.listdir(srcDir)
for filename in filenames:
    preFileName = filename.split(".")[0]
    if (preFileName[-1] == "A" or preFileName[-1] == "B" or preFileName[-1] == "C"):
        preFileName = preFileName[0:len(preFileName) - 1]
    destPicName = srcDir + os.sep + preFileName + '.jpg'
    if (os.path.isfile(destPicName)):
        print(destPicName + ' already here.\n')
    else:
        full_url = base_url + preFileName
        response = requests.get(full_url)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        try:
            imgsrc = soup.find(id = filterWord)['src']
            print(preFileName + "\n" + imgsrc)

            print(destPicName + "\n")
            if not (os.path.isfile(destPicName)):
                urllib.request.urlretrieve(imgsrc, destPicName)
        except:
            print('Can not find picture of ' + filename + '\n')