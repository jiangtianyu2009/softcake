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

        for job in list(project.jobs.iter_last(
                spider='javdetail', state='finished')):
            javjob = job

        print(javjob['key'])
        job = project.jobs.get(javjob['key'])

        for item in job.items.iter():
            if b'code' in item.keys():
                code = str(item[b'code'], 'utf-8')
                date = str(item[b'date'], 'utf-8')
            else:
                code = item['code']
                date = item['date']
            JavorderSpider.output.append({'code': code, 'date': date})
        JavorderSpider.output.sort(key=lambda x: x['date'], reverse=True)
        JavorderSpider.start_urls.append(TEST_URL)

    def parse(self, response):
        for out in JavorderSpider.output:
            yield {
                'code': out['code'],
                'date': out['date'],
            }
