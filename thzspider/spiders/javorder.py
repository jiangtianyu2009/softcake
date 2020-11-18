# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient

NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
CODE_FILTER_URL = ('https://raw.githubusercontent.com/bsonnier/'
                   'bsonnier.github.io/master/docs/codefilter')
BASE_URL = 'https://www.javlibrary.com/tw/'
TEST_URL = 'https://github.com/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavorderSpider(scrapy.Spider):
    name = 'javorder'
    start_urls = []
    output = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY)
        project = client.get_project(PROJECT_ID)

        for detailjob in list(project.jobs.iter_last(
                spider='javdetail', state='finished')):
            javdetailjob = detailjob
        print(javdetailjob['key'])
        detailjob = project.jobs.get(javdetailjob['key'])

        for code_job in list(project.jobs.iter_last(
                spider='javcode', state='finished')):
            jav_code_job = code_job
        print(jav_code_job['key'])
        code_job = project.jobs.get(jav_code_job['key'])

        tmp_output = []
        for item in detailjob.items.iter(count=10):
            if b'code' in item.keys():
                code = str(item[b'code'], 'utf-8')
                date = str(item[b'date'], 'utf-8')
            else:
                code = item['code']
                date = item['date']
            tmp_output.append({'code': code, 'date': date})
        tmp_output.sort(key=lambda x: x['date'], reverse=True)
        print(tmp_output)

        for tmp_item in tmp_output:
            filters = [("code", "=", [tmp_item['code']])]
            for item in code_job.items.iter(count=1, filter=filters):
                if b'code' in item.keys():
                    code = str(item[b'code'], 'utf-8')
                    date = str(tmp_item[b'date'], 'utf-8')
                    text = str(item[b'text'], 'utf-8')
                    name = str(item[b'name'], 'utf-8')
                    link = str(item[b'link'], 'utf-8')
                    down = str(item[b'down'], 'utf-8')
                    imgs = str(item[b'imgs'], 'utf-8')
                    imgl = str(item[b'imgl'], 'utf-8')
                else:
                    code = item['code']
                    date = tmp_item['date']
                    text = item['text']
                    name = item['name']
                    link = item['link']
                    down = item['down']
                    imgs = item['imgs']
                    imgl = item['imgl']
            JavorderSpider.output.append({'code': code, 'date': date,
                                          'text': text, 'name': name,
                                          'link': link, 'down': down,
                                          'imgs': imgs, 'imgl': imgl})

        JavorderSpider.start_urls.append(TEST_URL)

    def parse(self, response):
        for out in JavorderSpider.output:
            yield {
                'code': out['code'],
                'date': out['date'],
                'text': out['text'],
                'name': out['name'],
                'link': out['link'],
                'down': out['down'],
                'imgs': out['imgs'],
                'imgl': out['imgl'],
            }
