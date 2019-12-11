# -*- coding: utf-8 -*-
from scrapy import Spider,Request


class DoubanSpider(Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']
    start_url = 'https://movie.douban.com/subject/24852545/comments?limit=20&sort=new_score&status=P&start='
    
    def start_requests(self):
        print ('正在调用start_requests')
        for page in range(self.settings.get('MAXPAGE')):
            seen_url = self.start_url + str(page*20)
            print ('即将请求的url: ',seen_url)
            yield Request(url=seen_url,callback=self.parse,dont_filter=True)
    
    def parse(self, response):
        print ('正在回调parse')
        print (response.status)
