# -*- coding: utf-8 -*-
from scrapy import Spider,Request

class TieluSpider(Spider):
    name = 'tielu'
    allowed_domains = ['kyfw.12306.cn/otn/leftTicket/init']
    start_urls = ['http://kyfw.12306.cn/otn/leftTicket/init/']
    start_url = 'http://kyfw.12306.cn/otn/leftTicket/init/'

    def start_requests(self):
        for start_city in self.settings.get('STARTCITYLIST'):
            for end_city in self.settings.get('ENDCITYLIST'):
                yield Request(url=self.start_url,meta={'start_city':start_city,'end_city':end_city},dont_filter=True)

    def parse(self, response):
        print (response.text)
