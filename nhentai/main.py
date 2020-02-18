import nhentai_login_logout
import requests


login_url = 'https://nhentai.net/login/'
favor_url = 'https://nhentai.net/favorites/'
username = 'mjyang'
password = '3752926tianyu'

session = requests.Session()
nhentai_login_logout.nhentai_login(session, login_url, username, password)
