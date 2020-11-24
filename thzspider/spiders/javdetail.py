# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient


API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavdetailSpider(scrapy.Spider):
    name = 'javdetail'
    start_urls = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)

        for job in list(project.jobs.iter_last(
                spider='javcode', state='finished')):
            javjob = job

        print(javjob['key'])
        job = project.jobs.get(javjob['key'])

        for item in job.items.iter():
            link_detail = item['link']
            JavdetailSpider.start_urls.append(link_detail)

    def parse(self, response):
        video_id = response.css(
            'div[id="video_id"] .text::text').extract_first()
        video_date = response.css(
            'div[id="video_date"] .text::text').extract_first()
        yield {
            'code': video_id,
            'date': video_date,
        }
