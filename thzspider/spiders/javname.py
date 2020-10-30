# -*- coding: utf-8 -*-
import string

import requests
import scrapy


class JavnameSpider(scrapy.Spider):
    name = "javname"
    start_urls = []

    def __init__(self):
        baseurl = 'http://www.javlibrary.com/tw/'
        for word in string.ascii_uppercase:
            JavnameSpider.start_urls.append(
                baseurl + 'star_list.php?prefix=' + word)

    def parse(self, response):
        for searchitem in response.css('div.searchitem'):
            yield {
                'rfid': searchitem.css('::attr("id")').extract_first(),
                'name': searchitem.css('a::text').extract_first(),
                'href': searchitem.css('a::attr("href")').extract_first(),
            }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
