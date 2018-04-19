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

pdat = [
    "\r\n\u7247\u540d\uff1a\u304a\u307e\u25cb\u3053\u30fb\u30a2\u30ca\u30eb\u898b\u305b\u3064\u3051\u6311\u767a",
    "\r\n\u5bb9\u91cf\uff1a3.65GB",
    "\r\n\u683c\u5f0f\uff1amp4",
    "\r\n\u914d\u4fe1\u958b\u59cb\u65e5\uff1a\u00a0 \u00a0 \u00a0 \u00a0 2018/04/08",
    "\r\n\u5546\u54c1\u767a\u58f2\u65e5\uff1a\u00a0 \u00a0 \u00a0 \u00a0 2018/04/13",
    "\r\n\u53ce\u9332\u6642\u9593\uff1a\u00a0 \u00a0 \u00a0 \u00a0 126\u5206 \uff08HD\u7248\uff1a126\u5206\uff09",
    "\r\n\u51fa\u6f14\u8005\uff1a\u00a0 \u00a0 \u00a0 \u00a0 \u3042\u304a\u3044\u308c\u306a \u661f\u5cf6\u308b\u308a \u6d5c\u5d0e\u771f\u7dd2 \u3042\u305a\u5e0c \u7d50\u83dc\u306f\u308b\u304b \u82d1\u7530\u3042\u3086\u308a \u767d\u91d1\u308c\u3044\u5948 \u6cc9\u306e\u306e\u304b \u96ea\u7f8e\u3048\u307f\u308b \u7be0\u5d0e\u307f\u304a \u25bc\u3059\u3079\u3066\u8868\u793a\u3059\u308b",
    "\r\n\u76e3\u7763\uff1a\u00a0 \u00a0 \u00a0 \u00a0 ----",
    "\r\n\u30b7\u30ea\u30fc\u30ba\uff1a\u00a0 \u00a0 \u00a0 \u00a0 ----",
    "\r\n\u30e1\u30fc\u30ab\u30fc\uff1a\u00a0 \u00a0 \u00a0 \u00a0 \u30a2\u30ed\u30de\u4f01\u756b",
    "\r\n\u30ec\u30fc\u30d9\u30eb\uff1a\u00a0 \u00a0 \u00a0 \u00a0 AROMA",
    "\r\n\u30b8\u30e3\u30f3\u30eb\uff1a\u00a0 \u00a0 \u00a0 \u00a0 \u30cf\u30a4\u30d3\u30b8\u30e7\u30f3\u00a0\u00a0\u7368\u5360\u914d\u4fe1\u00a0\u00a0\u30df\u30cb\u30b9\u30ab\u00a0\u00a0\u7661\u5973\u00a0\u00a0\u4e3b\u89b3\u00a0\u00a0\u30a2\u30ca\u30eb\u00a0\u00a0\u5c40\u90e8\u30a2\u30c3\u30d7",
    "\r\n\u54c1\u756a\uff1a\u00a0 \u00a0 \u00a0 \u00a0 arm00667",
    "\r\n\r\n"
]

pday = "2011/01/01"
p = re.compile(r'(201[0-9]/[0-1][0-9]/[0-3][0-9])')
for line in pdat:
    res = p.search(line)
    if res:
        pday = res.group(1)
print(pday)
