# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient

BASE_URL = 'https://nhentai.net/language/chinese/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class NhtchnSpider(scrapy.Spider):
    name = 'nhtchn'
    start_urls = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)

        NhtchnSpider.start_urls.append(BASE_URL)

    def parse(self, response):
        for codeitem in response.css('div.container.index-container'):
            for galleryitem in codeitem.css('div.gallery'):
                gallery_href = galleryitem.css('a::attr(href)').extract_first()
                # id_code = codeitem.css('div.id::text').extract_first()
                # href_link = codeitem.css('a::attr(href)').extract_first()
                # img_small = codeitem.css('img::attr(src)').extract_first()
                yield {
                    'href': gallery_href,
                }
        # next_page = response.css('a.next::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
