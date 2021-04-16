# -*- coding: utf-8 -*-
import requests
import scrapy

BASE_URL = 'https://libraries.io/search?order=desc&per_page=100&platforms=PyPI&sort=dependent_repos_count&page='


class LibIOSpider(scrapy.Spider):
    name = 'libio'
    start_urls = []
    pkg_names = []

    def __init__(self):
        LibIOSpider.start_urls.append(BASE_URL + '2')

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
