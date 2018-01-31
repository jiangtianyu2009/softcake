import scrapy
import requests
from scrapinghub import ScrapinghubClient


class CodeSpider(scrapy.Spider):
    name = "javcode"
    baseurl = 'http://www.javlibrary.com/tw/'
    start_urls = []

    apikey = '11befd9da9304fecb83dfa114d1926e9'
    client = ScrapinghubClient(apikey)
    project = client.get_project(252342)

    for job in list(project.jobs.iter_last(spider='javname', state='finished')):
        javjob = job

    print(javjob['key'])
    job = project.jobs.get(javjob['key'])

    namelisturl = r'http://www.jiangtianyu.ga/assets/doc/namelist'
    namelist = requests.get(namelisturl).text.split('\n')
    print(namelist)

    codefilterurl = r'http://www.jiangtianyu.ga/assets/doc/codefilter'
    filterlist = requests.get(codefilterurl).text.split('\n')
    print(filterlist)

    for actorname in namelist:
        filters = [("name", "=", [actorname])]
        for item in job.items.iter(count=1, filter=filters):
            start_urls.append(baseurl + item['href'])

    def parse(self, response):

        acname = response.css('div.boxtitle::text').extract_first().split(' ')[0],

        for codeitem in response.css('div.video'):
            text = codeitem.css('div.title::text').extract_first()
            hasfilterword = False
            for filterword in CodeSpider.filterlist:
                if filterword in text:
                    hasfilterword = True
            if not hasfilterword:
                yield {
                    'code': codeitem.css('div.id::text').extract_first(),
                    'text': codeitem.css('div.title::text').extract_first(),
                    'name': acname,
                }

        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
