import scrapy


class ThzSpider(scrapy.Spider):
    name = "thzride"
    start_urls = [
        'http://thz.la/forum-220-1.html',
    ]

    def parse(self, response):

        for new in response.css('th.new'):
            text_new = new.css('a.xst::text').extract_first()
            href_new = 'http://thz.la/' + \
                new.css('a.xst::attr("href")').extract_first()
            yield {
                'text': text_new,
                'href': href_new,
            }

        for common in response.css('th.common'):
            text_common = common.css('a.xst::text').extract_first()
            href_common = 'http://thz.la/' + \
                common.css('a.xst::attr("href")').extract_first()
            yield {
                'text': text_common,
                'href': href_common,
            }

        next_page = response.css('a.nxt::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
