# -*- coding: utf-8 -*-
import requests
import scrapy
from scrapinghub import ScrapinghubClient

NAME_LIST_URL = ('https://raw.githubusercontent.com/bsonnier/'
                 'bsonnier.github.io/master/docs/namelist')
CODE_FILTER_URL = ('https://raw.githubusercontent.com/bsonnier/'
                   'bsonnier.github.io/master/docs/codefilter')


class JavcodeSpider(scrapy.Spider):
    name = 'javcode'
    start_urls = []
    filterlist = []
    namelist = []

    def __init__(self):
        baseurl = 'http://www.javlibrary.com/tw/'
        apikey = '11befd9da9304fecb83dfa114d1926e9'
        client = ScrapinghubClient(apikey)
        project = client.get_project(252342)

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
                actor_url = baseurl + item['href']
                print(actorname + '\n' + actor_url)
                JavcodeSpider.start_urls.append(actor_url)

    def parse(self, response):
        acname = response.css('div.boxtitle::text').extract_first().split()[0]
        for codeitem in response.css('div.video'):
            text = codeitem.css('div.title::text').extract_first()
            code = codeitem.css('div.id::text').extract_first()
            hasfilterword = False
            for filterword in JavcodeSpider.filterlist:
                if filterword in text:
                    hasfilterword = True
                if filterword in code:
                    hasfilterword = True
            if not hasfilterword:
                yield {
                    'code': code,
                    'text': text,
                    'name': acname,
                }
        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
