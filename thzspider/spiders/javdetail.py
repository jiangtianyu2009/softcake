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

        for jav_code_job in list(project.jobs.iter_last(
                spider='javcode', state='finished')):
            jav_job = jav_code_job

        print(jav_job['key'])
        jav_code_job = project.jobs.get(jav_job['key'])

        for item in jav_code_job.items.iter():
            link_detail = item['link']
            JavdetailSpider.start_urls.append(link_detail)

        JavdetailSpider.start_urls = list(set(JavdetailSpider.start_urls))

    def parse(self, response):
        video_id = response.css(
            'div[id="video_id"] .text::text').extract_first()
        video_date = response.css(
            'div[id="video_date"] .text::text').extract_first()
        video_maker = response.css('span.maker .a::text').extract_first()
        yield {
            'code': video_id,
            'date': video_date,
            'makr': video_maker,
        }
