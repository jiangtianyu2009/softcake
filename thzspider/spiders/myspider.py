import scrapy


class ThzSpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        'http://thz.la/forum-220-1.html',
    ]

    def parse(self, response):

        for new in response.css('th.new'):
            href_new = new.css('a.xst::attr("href")').extract_first()
            yield response.follow(href_new, self.getdetail)

        for common in response.css('th.common'):
            href_common = common.css('a.xst::attr("href")').extract_first()
            yield response.follow(href_common, self.getdetail)

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def getdetail(self, response):
        text = response.css('h1.ts span::text').extract_first()
        imgf = response.css('img.zoom::attr("file")').extract_first()
        yield {
            'text': text,
            'href': response.url,
            'imgf': imgf,
        }
