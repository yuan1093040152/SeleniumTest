# -*- coding: utf-8 -*-
import scrapy


class BaiduComSpider(scrapy.Spider):
    name = 'baidu.com'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
