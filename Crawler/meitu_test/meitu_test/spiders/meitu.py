# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from urllib.parse import urlencode
from meitu_test.items import MeituItem
import json,time

class MeituiSpider(Spider):
    name = 'meitu'
    allowed_domains = ['image.so.com']
    start_urls = ['http://images.so.com/']
    max_page = 30

    def start_requests(self):
        print ('开始调用')
        data = {'ch': 'photography','listtype': 'new','temp': '1'}
        seen_url = 'https://image.so.com/zj?'
        for page in range(1,self.max_page + 1):
            data['sn'] = page *30
            url = seen_url + urlencode(data)
            yield Request(url=url,callback=self.parse)
                
    def parse(self,response):
        item = MeituItem()
        result = json.loads(response.text)
        images = result.get('list')
        for image in images:
            item['id'] = image.get('imageid')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item
    
            
            

