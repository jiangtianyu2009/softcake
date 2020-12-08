# This program is used for rename the video downloaded from YouKu

import os

dir = 'C:\\Users\\JIANG\\Downloads'
filenames = os.listdir(dir)

for file in filenames:
    if "—" in file:
        print("%s %d\n" % ("Start Index: ", file.index("—")))
        if "2.flv" in file:
            os.rename(dir + os.sep + file, dir + os.sep +
                      file[0:file.index("—")] + '2.flv')
        else:
            os.rename(dir + os.sep + file, dir + os.sep +
                      file[0:file.index("—")] + '.flv')
