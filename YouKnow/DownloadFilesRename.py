import os
import re

p = re.compile(r'(\D+\d+)(\w*)(.\w+)')
distDirList = [r'E:\tempe\TC', r'F:\tempf\TC',
               r'G:\tempg\TC']

for distDir in distDirList:
    filenames = os.listdir(distDir)
    upperfilenames = []
    print(filenames)
    for filenamepref in filenames:
        if filenamepref.find('_') > 0:
            filenameprefit = filenamepref[filenamepref.index('_'):]
        else:
            filenameprefit = filenamepref
        filenamepost = filenameprefit.replace('-', '').replace('_', '')\
            .replace(' ', '').replace('.1080p', '').replace('.720p', '')\
            .replace('[thz.la]', '').replace('[Thz.la]', '').replace('[HD]', '')\
            .replace('cd1', 'A').replace('cd2', 'B')
        fhalf = p.search(filenamepost).group(1).upper()
        mhalf = p.search(filenamepost).group(2).upper()
        lhalf = p.search(filenamepost).group(3).lower()
        if mhalf == "A" or mhalf == "B" or mhalf == "C":
            distname = fhalf + mhalf + lhalf
        else:
            distname = fhalf + lhalf
        print(distname)
        os.rename(distDir + os.sep + filenamepref, distDir + os.sep + distname)
