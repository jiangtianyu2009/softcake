import os
import sys

(dir, filename) = os.path.split(os.path.abspath(sys.argv[0]))
print(dir)
print(filename)

filenames = os.listdir(dir)
for file in filenames:
    print(file)