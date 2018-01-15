import scrapy
import urllib
from scrapinghub import ScrapinghubClient


class CodeSpider(scrapy.Spider):
    name = "javcode"
    baseurl = 'http://www.j17v.com/cn/'
    start_urls = []

    apikey = '11befd9da9304fecb83dfa114d1926e9'
    client = ScrapinghubClient(apikey)
    project = client.get_project(252342)

    for job in list(project.jobs.iter_last(spider='javname', state='finished')):
        javjob = job

    print(javjob['key'])
    job = project.jobs.get(javjob['key'])

    namelisturl = r'http://www.jiangtianyu.ga/assets/doc/namelist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=namelisturl, headers=headers)
    namelist = urllib.request.urlopen(req).read().decode('utf-8').split("\n")

    for actorname in namelist:
        filters = [("name", "=", [actorname])]
        for item in job.items.iter(count=1, filter=filters):
            start_urls.append(baseurl + item['href'])

    def parse(self, response):

        for codeitem in response.css('div.id'):
            yield {
                'code': codeitem.css('::text').extract_first(),
            }

        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
