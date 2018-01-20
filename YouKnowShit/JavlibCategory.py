import requests
import bs4
import os
import shutil
import re

base_url = 'http://www.javlibrary.com/tw/vl_searchbyid.php?keyword='
srcDir = r'H:\TCtemp1'
distDir = r'H:\TCtemp2'
favstarsFile = r'C:\Users\jiang\Downloads\favstars-mjyang-1516433213.html'
favstarsList = []
filterWord = "演員:"

htmlfile = open(favstarsFile, 'r', encoding='UTF-8')
htmltext = htmlfile.read()
soup = bs4.BeautifulSoup(htmltext, "html.parser")
for actName in soup.select('span'):
    favstarsList.append(actName.string)

filenames = os.listdir(srcDir)
if not os.path.isdir(distDir):
    os.mkdir(distDir)

for filename in filenames:
    preFileName = filename.split(".")[0]
    if preFileName[-1] == "A" or preFileName[-1] == "B" or preFileName[-1] == "C":
        preFileName = preFileName[0:len(preFileName) - 1]
    full_url = base_url + preFileName
    response = requests.get(full_url)
    if filterWord in response.text:
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        nameParag = soup.findAll(text=re.compile(filterWord))[0].parent.parent
        if not len(nameParag.select('a')) == 0:
            actorNameDir = nameParag.a.string
            for actNameThis in nameParag.select('a'):
                if os.path.isdir(distDir + os.sep + actNameThis.string):
                    actorNameDir = actNameThis.string
                    break
                if actNameThis.string in favstarsList:
                    actorNameDir = actNameThis.string
                    break
            if not os.path.isdir(distDir + os.sep + actorNameDir):
                os.mkdir(distDir + os.sep + actorNameDir)
            shutil.move(srcDir + os.sep + filename,
                        distDir + os.sep + actorNameDir)
            print('Moving ' + filename + ' to directory ' + actorNameDir)
