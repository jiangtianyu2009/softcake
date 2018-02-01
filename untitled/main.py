__author__ = 'toby'


class student:
    name = ''
    num = 0
    grade = 0

    def __init__(self, pname, pnum, pgrade):
        self.name = pname
        self.num = pnum
        self.grade = pgrade


file_object = open('a.txt')
s = []
try:
    i = 0
    text = file_object.readline()
    while (text != ''):
        s.append(student(text.split(' ')[1], text.split(
            ' ')[0], text.split(' ')[2].strip('\n')))
        i = i + 1
        text = file_object.readline()
finally:
    file_object.close()

for si in s:
    print si.name
