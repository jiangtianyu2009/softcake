import requests
from bs4 import BeautifulSoup

baseurl = BeautifulSoup(requests.get('http://www.javlib.com/').text,
                        "lxml").find_all('a', 'enter')[2].get("href") + '/'
print(baseurl)
