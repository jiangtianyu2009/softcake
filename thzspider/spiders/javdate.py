# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient

NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
CODE_FILTER_URL = ('https://raw.githubusercontent.com/bsonnier/'
                   'bsonnier.github.io/master/docs/codefilter')
BASE_URL = 'https://www.javlibrary.com/tw/'
BT_URL = 'https://btsow.work/search/'
API_KEY = '11befd9da9304fecb83dfa114d1926e9'
PROJECT_ID = '252342'


class JavdateSpider(scrapy.Spider):
    name = 'javdate'
    start_urls = []
    filterlist = []
    namelist = []

    def __init__(self):
        client = ScrapinghubClient(API_KEY)
        project = client.get_project(PROJECT_ID)

        for job in list(project.jobs.iter_last(
                spider='javname', state='finished')):
            javjob = job

        print(javjob['key'])
        job = project.jobs.get(javjob['key'])

        JavdateSpider.namelist = requests.get(
            NAME_LIST_URL).text.split('\n')
        print(JavdateSpider.namelist)

        JavdateSpider.filterlist = requests.get(
            CODE_FILTER_URL).text.split('\n')
        print(JavdateSpider.filterlist)

        for actorname in JavdateSpider.namelist:
            filters = [("name", "=", [actorname])]
            for item in job.items.iter(count=1, filter=filters):
                # Network transfer will use bytes data like this:
                # b'name': b'\xe7\xa7\x8b\xe5\xb1\xb1\xe7\xa5\xa5\xe5\xad\x90',
                # b'href': b'vl_star.php?s=aqja',
                print(item)
                if b'hrel' in item.keys():
                    actor_url = str(item[b'hrel'], 'utf-8')
                else:
                    actor_url = item['hrel']
                print(actorname + '\n' + actor_url)
                JavdateSpider.start_urls.append(actor_url)

    def parse(self, response):
        for codeitem in response.css('td.title'):
            title_text = codeitem.css('td::text').extract_first()
            print(title_text)
            hasfilterword = False
            for filterword in JavdateSpider.filterlist:
                if filterword in title_text:
                    hasfilterword = True
                if filterword in id_code:
                    hasfilterword = True
            if not hasfilterword:
                yield {
                    'text': title_text,
                }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
