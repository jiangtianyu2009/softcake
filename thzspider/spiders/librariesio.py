# -*- coding: utf-8 -*-
import scrapy

BASE_URL = 'https://libraries.io/search?order=desc&per_page=100&platforms=PyPI&sort=rank&page='


class LibIOSpider(scrapy.Spider):
    name = 'libio'
    start_urls = []
    pkg_names = []
    page_num = 1

    def __init__(self):
        LibIOSpider.start_urls.append(BASE_URL + str(self.page_num))

    def parse(self, response):
        for codeitem in response.css('div.project'):
            pkg_name = codeitem.css('a::text').extract_first()
            LibIOSpider.pkg_names.append(pkg_name)
            yield {
                'name': pkg_name,
            }
        print(LibIOSpider.pkg_names)
        f = open("requirements.txt", "w+")
        for name in LibIOSpider.pkg_names:
            f.write(name + '\n')
        f.close()
        if self.page_num < 10:
            self.page_num += 1
            new_url = BASE_URL + str(self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
