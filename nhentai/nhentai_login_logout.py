import requests
import re
import chardet
import time


def parse_csrfmiddlewaretoken(content):
    csrf_regex = r'<input type="hidden" name="csrfmiddlewaretoken" value="(.*)">'
    csrf_pattern = re.compile(csrf_regex)
    encode_type = chardet.detect(content)
    csrfmiddlewaretoken = csrf_pattern.findall(
        content.decode(encode_type['encoding']))[0]
    print('csrfmiddlewaretoken' + ' = ' + csrfmiddlewaretoken)
    return csrfmiddlewaretoken


def nhentai_login(login_session, login_url, username, password):
    my_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,pt;q=0.6',
        'cookie': ''
    }

    # Get token
    login_response = login_session.get(login_url, headers=my_headers)
    csrfmiddlewaretoken = parse_csrfmiddlewaretoken(login_response.content)

    # Post data
    my_data = {
        'csrfmiddlewaretoken': csrfmiddlewaretoken,
        'username_or_email': username,
        'password': password
    }

    # Get response
    for cookieItem in login_session.cookies.items():
        my_headers['cookie'] = my_headers['cookie'] + cookieItem[0] + '=' + cookieItem[1] + ';'
        print(cookieItem[0] + ' = ' + cookieItem[1])
    
    time.sleep(5)

    r = login_session.post(login_url, data=my_data,
                           headers=my_headers)

    print(r.content)

    return login_session
