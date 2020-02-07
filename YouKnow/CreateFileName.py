import os

srcDir = "G:\\else\\TC"
distDir = "C:\\Users\\JIANG\\Downloads\\FileNameData"
filenames = os.listdir(srcDir)

for filename in filenames:
    if ".jpg" not in filename:
        fp = open(distDir + os.sep + filename, "w")
        fp.write(filename)
        fp.close()
