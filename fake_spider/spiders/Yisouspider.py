# -*- coding=utf-8 -*-
from scrapy import Request
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy_redis.spiders import RedisSpider
from scrapy.contrib.spiders import CrawlSpider
import re


class YisouSpider(CrawlSpider):
    name = 'YisouSpider'
    start_urls = ['http://mai.958shop.com/cluwoshijia1']

    def parse(self, response):
        for num in range(0, 100):
            url = 'http://mai.958shop.com/cluxxx%s' % num
            print(url)
            yield Request(url=url, callback=self.next_parse)

    def next_parse(self, response):
        sell = Selector(response)
        head = sell.xpath('//title/text()').extract()[0]
        print(head)


