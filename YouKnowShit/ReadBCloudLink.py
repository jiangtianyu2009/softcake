import os
import re

distDir = 'F:\\utorrent\\dllink'


filenames = os.listdir(distDir)
print(filenames)

for filename in filenames:
    dlurl = "http://pan.baidu.com/s/" + \
        open(distDir + os.sep + filename,
             "r").readline().split('/')[4].split(' ')[0]
    flpwd = open(distDir + os.sep + filename, "r").readline()[-4:]
    print(dlurl + '  ' + flpwd)
