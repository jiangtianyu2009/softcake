import os
import sys

(dir, filename) = os.path.split(os.path.abspath(sys.argv[0]))
print(dir)
updir = os.path.abspath('..')
print(updir)
os.chdir(updir)
upupdir = os.path.abspath('..')
print(upupdir)
os.chdir(upupdir)
upupupdir = os.path.abspath('..')
print(upupupdir)
print(filename)


filenames = os.listdir(dir)
for file in filenames:
    print(file)