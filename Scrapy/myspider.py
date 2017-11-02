import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://thibt.com/forum-220-1.html',
    ]

    def parse(self, response):
        for quote in response.css('th.common'):
            yield {
                'text': quote.css('a.xst::text').extract_first(),
                'href': quote.css('a.xst::attr("href")').extract_first(),
            }

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
