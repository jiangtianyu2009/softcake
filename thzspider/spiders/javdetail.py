# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient

NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
CODE_FILTER_URL = ('https://raw.githubusercontent.com/bsonnier/'
                   'bsonnier.github.io/master/docs/codefilter')
BASE_URL = 'https://www.javlibrary.com/tw/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavdetailSpider(scrapy.Spider):
    name = 'javdetail'
    start_urls = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY)
        project = client.get_project(PROJECT_ID)

        for job in list(project.jobs.iter_last(
                spider='javcode', state='finished')):
            javjob = job

        print(javjob['key'])
        job = project.jobs.get(javjob['key'])

        for item in job.items.iter(count=1):
            # Network transfer will use bytes data like this:
            # b'name': b'\xe7\xa7\x8b\xe5\xb1\xb1\xe7\xa5\xa5\xe5\xad\x90',
            # b'href': b'vl_star.php?s=aqja',
            print(item)
            if b'link' in item.keys():
                link_detail = str(item[b'link'], 'utf-8')
            else:
                link_detail = item['link']
            print(link_detail)
            JavdetailSpider.start_urls.append(link_detail)

    def parse(self, response):
        print("start parse---------")
        video_id = response.css(
            'div[id="video_id"] .text::text').extract_first()
        video_date = response.css(
            'div[id="video_date"] .text::text').extract_first()
        print(video_id)
        print(video_date)
        yield {
            'code': video_id,
            'date': video_date,
        }
