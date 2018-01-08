import scrapy
import string


class NameSpider(scrapy.Spider):
    name = "javname"
    baseurl = 'http://www.j17v.com/cn/star_list.php?prefix='
    start_urls = []
    for word in string.ascii_uppercase:
        start_urls.append(baseurl + word)

    def parse(self, response):

        for searchitem in response.css('div.searchitem'):
            yield {
                'rfid': searchitem.css('::attr("id")').extract_first(),
                'name': searchitem.css('a::text').extract_first(),
                'href': searchitem.css('a::attr("href")').extract_first(),
            }

        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
