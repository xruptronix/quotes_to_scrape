# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from quotes_spider.items import QuotesSpiderItem

class ExampleSpider(Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(),response=response)
        heading = response.xpath("//h1/text()").extract_first()
        link = response.xpath("//a/@href").extract_first()

        l.add_value('heading',heading)
        l.add_value('link',link)
        return l.load_item()
