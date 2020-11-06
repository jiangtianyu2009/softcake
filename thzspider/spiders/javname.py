# -*- coding: utf-8 -*-
import string

import requests
import scrapy

BASE_URL = 'https://www.javlibrary.com/tw/'


class JavnameSpider(scrapy.Spider):
    name = "javname"
    start_urls = []

    def __init__(self):
        for word in string.ascii_uppercase:
            JavnameSpider.start_urls.append(
                BASE_URL + 'star_list.php?prefix=' + word)

    def parse(self, response):
        for searchitem in response.css('div.searchitem'):
            reference_id = searchitem.css('::attr("id")').extract_first()
            actor_name = searchitem.css('a::text').extract_first()
            href_link = searchitem.css('a::attr("href")').extract_first()
            yield {
                'rfid': reference_id,
                'name': actor_name,
                'href': BASE_URL + href_link,
            }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
