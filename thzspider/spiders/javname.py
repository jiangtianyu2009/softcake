# -*- coding: utf-8 -*-
import string

import requests
import scrapy

BASE_URL = 'https://www.javlibrary.com/tw/'
NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')


class JavnameSpider(scrapy.Spider):
    name = "javname"
    start_urls = []
    namelist = []

    def __init__(self):
        JavnameSpider.namelist = requests.get(
            NAME_LIST_URL).text.split()
        print(JavnameSpider.namelist)
        for word in string.ascii_uppercase:
            JavnameSpider.start_urls.append(
                BASE_URL + 'star_list.php?prefix=' + word)

    def parse(self, response):
        for searchitem in response.css('div.searchitem'):
            actor_name = searchitem.css('a::text').extract_first()
            if actor_name in JavnameSpider.namelist:
                reference_id = searchitem.css('::attr("id")').extract_first()
                href_link = searchitem.css('a::attr("href")').extract_first()
                yield {
                    'rfid': reference_id,
                    'name': actor_name,
                    'href': BASE_URL + href_link,
                    'hrel': BASE_URL + href_link.replace("php?", "php?list&"),
                }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
