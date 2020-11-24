# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient


NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
CODE_FILTER_URL = ('https://raw.githubusercontent.com/bsonnier/'
                   'bsonnier.github.io/master/docs/codefilter')
BASE_URL = 'https://www.javlibrary.com/tw/'
BT_URL = 'https://btsow.com/search/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavcodeSpider(scrapy.Spider):
    name = 'javcode'
    start_urls = []
    filterlist = []
    namelist = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY, use_msgpack=False)
        project = client.get_project(PROJECT_ID)

        for job in list(project.jobs.iter_last(
                spider='javname', state='finished')):
            javjob = job

        print(javjob['key'])
        job = project.jobs.get(javjob['key'])

        JavcodeSpider.namelist = requests.get(
            NAME_LIST_URL).text.split('\n')
        print(JavcodeSpider.namelist)

        JavcodeSpider.filterlist = requests.get(
            CODE_FILTER_URL).text.split('\n')
        print(JavcodeSpider.filterlist)

        for actorname in JavcodeSpider.namelist:
            filters = [("name", "=", [actorname])]
            for item in job.items.iter(count=1, filter=filters):
                print(item)
                actor_url = item['href']
                print(actorname + '\n' + actor_url)
                JavcodeSpider.start_urls.append(actor_url)

    def parse(self, response):
        actor_name = response.css('div.boxtitle::text').extract_first()
        for codeitem in response.css('div.video'):
            title_text = codeitem.css('div.title::text').extract_first()
            id_code = codeitem.css('div.id::text').extract_first()
            href_link = codeitem.css('a::attr(href)').extract_first()
            img_small = codeitem.css('img::attr(src)').extract_first()
            hasfilterword = False
            for filterword in JavcodeSpider.filterlist:
                if filterword in title_text:
                    hasfilterword = True
                if filterword in id_code:
                    hasfilterword = True
            if not hasfilterword:
                yield {
                    'code': id_code,
                    'text': title_text,
                    'name': actor_name.split()[0],
                    'link': BASE_URL + href_link[2:],
                    'down': BT_URL + id_code,
                    'imgs': "https:" + img_small,
                    'imgl': "https:" + img_small.replace("ps.jpg", "pl.jpg"),
                }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
