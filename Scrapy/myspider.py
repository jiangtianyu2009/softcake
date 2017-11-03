import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://thibt.com/forum-220-1.html',
    ]

    def parse(self, response):

        for new in response.css('th.new'):
            yield {
                'text': new.css('a.xst::text').extract_first(),
                'href': new.css('a.xst::attr("href")').extract_first(),
            }

        for common in response.css('th.common'):
            yield {
                'text': common.css('a.xst::text').extract_first(),
                'href': common.css('a.xst::attr("href")').extract_first(),
            }

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
