import re

strss = '[abc-123]kajjgkkrk'
print(re.split(r'[\[\]]', strss)[1])


def builddlnk(href, dlnk):
    if r'imc_attachad-ad.html?' in dlnk:
        dlnk = dlnk.replace(r'imc_attachad-ad.html?',
                            r'forum.php?mod=attachment&')
    pre = re.split(r'[/]', href)[2]
    return 'http://' + pre + '/' + dlnk


dlnk = builddlnk("http://thz2.com/thread-1803898-1-1.html",
                 "imc_attachad-ad.html?aid=NDA3NzcyfGZkYmI1OGRlfDE1MjM1NDk3MTl8MHwxODAzODk4")
print(dlnk)
