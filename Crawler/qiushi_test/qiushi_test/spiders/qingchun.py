# -*- coding: utf-8 -*-
from scrapy import Request,Spider
from qiushi_test.items import QiushiItem
import json


class QingchunSpider(Spider):
    name = 'qingchun'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']
    start_url = 'http://image.so.com/j?q=%E6%B8%85%E7%BA%AF&pn=60&sn='
    
    def start_requests(self):
        for index in range(self.settings.get('MAXINDEX')):
            sn = 130 + index * 60
            yield Request(url=self.start_url + str(sn),callback=self.parse)
        

    def parse(self, response):
        item = QiushiItem()
        data = json.loads(response.text)
        images = data.get('list')
        for  image in images:
            item['image'] = image.get('img')
            yield item
