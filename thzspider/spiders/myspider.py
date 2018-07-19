# -*- coding: utf-8 -*-
import re

import requests
import scrapy
from bs4 import BeautifulSoup
from scrapinghub import ScrapinghubClient


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        'http://thz.la/forum-220-1.html',
    ]
    jav_url = ''
    codelist = []
    namelist = []

    def __init__(self):
        baseurl = BeautifulSoup(requests.get('http://www.javlib.com/').text,
                                "lxml").find_all('a', 'enter')[2].get("href") + '/'
        MyspiderSpider.jav_url = baseurl + 'vl_searchbyid.php?keyword='

        apikey = '11befd9da9304fecb83dfa114d1926e9'
        client = ScrapinghubClient(apikey)
        project = client.get_project(252342)

        for job in list(project.jobs.iter_last(spider='javcode', state='finished')):
            codejob = job

        print(codejob['key'])
        lastcodejob = project.jobs.get(codejob['key'])

        for item in lastcodejob.items.iter():
            MyspiderSpider.codelist.append(item['code'])
            MyspiderSpider.namelist.append(item['name'])

    def parse(self, response):

        for new in response.css('th.new'):
            try:
                code_new = re.split(r'[\[\]]', new.css(
                    'a.xst::text').extract_first())[1].upper()
                href_new = new.css('a.xst::attr("href")').extract_first()
                if code_new in MyspiderSpider.codelist:
                    name_new = MyspiderSpider.namelist[MyspiderSpider.codelist.index(
                        code_new)]
                    yield response.follow(href_new, self.getdetail, meta={'code': code_new, 'name': name_new})
            except Exception:
                pass

        for common in response.css('th.common'):
            try:
                code_common = re.split(r'[\[\]]', common.css(
                    'a.xst::text').extract_first())[1].upper()
                href_common = common.css('a.xst::attr("href")').extract_first()
                if code_common in MyspiderSpider.codelist:
                    name_common = MyspiderSpider.namelist[MyspiderSpider.codelist.index(
                        code_common)]
                    yield response.follow(href_common, self.getdetail, meta={'code': code_common, 'name': name_common})
            except Exception:
                pass

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def getdetail(self, response):
        code = response.meta['code']
        name = response.meta['name']
        text = response.css('h1.ts span::text').extract_first()
        imgf = response.css('img.zoom::attr("file")').extract_first()
        pdat = response.css('td.t_f::text').extract()
        try:
            pdat = pdat[:pdat.index('\r\n')]
        except:
            pass
        try:
            pdat = pdat[:pdat.index('\r\n\r\n')]
        except:
            pass
        try:
            dlnk = self.builddlnk(response.url, response.css(
                'p.attnm a::attr("href")').extract_first())
        except:
            dlnk = response.url

        yield {
            'code': code,
            'name': name[0],
            'text': text,
            'imgf': imgf,
            'jref': self.jav_url + code,
            'href': response.url,
            'dlnk': dlnk,
            'pdat': pdat,
            'pday': self.regxpday(pdat)
        }

    def builddlnk(self, href, dlnk):
        if r'imc_attachad-ad.html?' in dlnk:
            dlnk = dlnk.replace(r'imc_attachad-ad.html?',
                                r'forum.php?mod=attachment&')
        pre = re.split(r'[/]', href)[2]
        return 'http://' + pre + '/' + dlnk

    def regxpday(self, pdat):
        pday = "2011/01/01"
        p = re.compile(r'(201[0-9]/[0-1][0-9]/[0-3][0-9])')
        for line in pdat:
            res = p.search(line)
            if res:
                pday = res.group(1)
        return pday
