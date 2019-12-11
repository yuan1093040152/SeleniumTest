# -*- coding: utf-8 -*-
from scrapy import Spider,Request


class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']
    start_url = 'https://movie.douban.com/subject/24852545/comments?limit=20&sort=new_score&status=P&start='
    
    def start_requests(self):
        for page in range(self.settings.get('MAXPAGE')):
            yield Request(url=self.start_url + str(page*20),callback=self.parse)
    
    def parse(self, response):
        print (response.status)
