import scrapy
import re
from scrapinghub import ScrapinghubClient


class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        'http://thz.la/forum-220-1.html',
    ]
    codelist = []

    apikey = '11befd9da9304fecb83dfa114d1926e9'
    client = ScrapinghubClient(apikey)
    project = client.get_project(252342)

    for job in list(project.jobs.iter_last(spider='javcode', state='finished')):
        codejob = job

    print(codejob['key'])
    lastcodejob = project.jobs.get(codejob['key'])

    for item in lastcodejob.items.iter():
        codelist.append(item['code'])

    def parse(self, response):

        for new in response.css('th.new'):
            try:
                code_new = re.split(r'[\[\]]', new.css(
                    'a.xst::text').extract_first())[1].upper()
                href_new = new.css('a.xst::attr("href")').extract_first()
                if code_new in MySpider.codelist:
                    yield response.follow(href_new, self.getdetail, meta={'code': code_new})
            except Exception:
                pass

        for common in response.css('th.common'):
            try:
                code_common = re.split(r'[\[\]]', common.css(
                    'a.xst::text').extract_first())[1].upper()
                href_common = common.css('a.xst::attr("href")').extract_first()
                if code_common in MySpider.codelist:
                    yield response.follow(href_common, self.getdetail, meta={'code': code_common})
            except Exception:
                pass

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def getdetail(self, response):
        code = response.meta['code']
        text = response.css('h1.ts span::text').extract_first()
        imgf = response.css('img.zoom::attr("file")').extract_first()
        yield {
            'code': code,
            'text': text,
            'href': response.url,
            'imgf': imgf,
        }
