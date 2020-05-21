import os
import random
import re
import shutil
import threading
import time
import urllib.request
import bs4
import requests

base_url = 'https://avmoo.host/cn/search/'
srcDirList = [r'F:\tempg\TC', r'G:\tempg\TC']


def getImageName(fileName):
    fileNamePrefix = fileName.split(".")[0]
    if fileNamePrefix[-1] == "A" or fileNamePrefix[-1] == "B" or fileNamePrefix[-1] == "C":
        fileNamePrefix = fileNamePrefix[0:len(fileNamePrefix) - 1]
    return fileNamePrefix


def getAvDetail(fileNamePrefix):
    act_name = None
    # Get Search Page
    search_url = base_url + fileNamePrefix
    print('Search URL is: ' + search_url)
    search_response = requests.get(search_url)
    search_soup = bs4.BeautifulSoup(
        search_response.text, "html.parser")
    # Get Detail Page
    detail_url = search_soup.find(
        'a', {'class': "movie-box"})['href']
    print('Detail URL is: ' + detail_url)
    detail_response = requests.get(detail_url)
    detail_soup = bs4.BeautifulSoup(
        detail_response.text, "html.parser")
    # Get Image Src
    imgsrc = detail_soup.find('img')['src']
    print('Images URL is: ' + imgsrc)
    try:
        act_name = detail_soup.find(
            'a', {'class': "avatar-box"}).text.strip()
        print('Actor name is: ' + act_name)
    except:
        print('Cannot find actor name of ' + fileNamePrefix)
    return imgsrc, act_name


def downloadImage(fileName):
    fileNamePrefix = getImageName(fileName)
    destImagePath = srcDir + os.sep + fileNamePrefix + '.jpg'
    # Check Whether Image Exists
    if os.path.isfile(destImagePath):
        print(destImagePath + ' already here.\n')
    else:
        imgsrc, act_name = getAvDetail(fileNamePrefix)
        # Download Image
        print('Desti file path: ' + destImagePath)
        if not os.path.isfile(destImagePath):
            opener = urllib.request.build_opener()
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgsrc, destImagePath)
        print('=======================================')


def categoryImage(fileName):
    fileNamePrefix = getImageName(fileName)
    imgsrc, act_name = getAvDetail(fileNamePrefix)
    if act_name is not None:
        if not os.path.isdir(srcDir + 'C' + os.sep + act_name):
            os.mkdir(srcDir + 'C' + os.sep + act_name)
        shutil.move(srcDir + os.sep + fileName,
                    srcDir + 'C' + os.sep + act_name)
        print('Moving ' + fileName + ' to directory ' + act_name)


if __name__ == '__main__':

    for srcDir in srcDirList:
        fileNames = os.listdir(srcDir)
        for fileName in fileNames:
            downloadImage(fileName)
        for fileName in fileNames:
            categoryImage(fileName)
