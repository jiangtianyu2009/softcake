import os
import sys

(dir, filename) = os.path.split(os.path.abspath(sys.argv[0]))
print(dir)
filenames = os.listdir(dir)
for file in filenames:
    print(file)

print()
print()
print()
print('*****************************************************')
updir = os.path.abspath('..')
print(updir)
filenames = os.listdir(updir)
for file in filenames:
    print(file)

print()
print()
print()
print('*****************************************************')
os.chdir(updir)
upupdir = os.path.abspath('..')
print(upupdir)
filenames = os.listdir(upupdir)
for file in filenames:
    print(file)

print()
print()
print()
print('*****************************************************')
os.chdir(upupdir)
upupupdir = os.path.abspath('..')
print(upupupdir)
filenames = os.listdir(upupupdir)
for file in filenames:
    print(file)

print()
print()
print()
print('*****************************************************')
os.chdir(upupupdir)
upupupupdir = os.path.abspath('..')
print(upupupupdir)
filenames = os.listdir(upupupupdir)
for file in filenames:
    print(file)
