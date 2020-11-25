# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient


TEST_URL = 'https://github.com/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavorderSpider(scrapy.Spider):
    name = 'javorder'
    start_urls = []
    output = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)

        # Get detail job
        for detail_job in list(project.jobs.iter_last(
                spider='javdetail', state='finished')):
            jav_detail_job = detail_job
        print(jav_detail_job['key'])
        detail_job = project.jobs.get(jav_detail_job['key'])

        # Get code job
        for code_job in list(project.jobs.iter_last(
                spider='javcode', state='finished')):
            jav_code_job = code_job
        print(jav_code_job['key'])
        code_job = project.jobs.get(jav_code_job['key'])

        # Sort detail items by date
        tmp_output = []
        for item in detail_job.items.iter():
            code = item['code']
            date = item['date']
            tmp_output.append({'code': code, 'date': date})
        tmp_output.sort(key=lambda x: x['date'], reverse=True)

        # Fullfill detail items
        for tmp_item in tmp_output[:1000]:
            filters = [("code", "=", [tmp_item['code']])]
            for item in code_job.items.iter(filter=filters):
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

        # Mock start urls
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
