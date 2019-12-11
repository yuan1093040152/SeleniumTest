# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from qiushi_test.items import QiushiItem
import requests



class QiushiSpider(Spider):
    name = 'qiushi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']
    start_url = 'http://www.qiushibaike.com'
    
    def start_requests(self):
        yield Request(url=self.start_url,callback=self.parse,meta={'download_timeout':10},dont_filter=True)
    
    def parse(self, response):
        pass
        item = QiushiItem()
        qiushilist = response.css('.content-block>#content-left>div')
        for qiushi in qiushilist:
            try:
                item['head_image'] = 'http:' + qiushi.css('.author>a>img::attr(src)').extract_first()
                item['name'] = qiushi.css('.author>a>h2::text').extract_first()
                item['content'] = qiushi.css('.content>span::text').extract_first()
                gender_attr = qiushi.css('.author>div::attr(class)').extract_first()
                if 'manIcon' in gender_attr:
                    item['gender'] = 'man'
                elif 'womenIcon' in gender_attr:
                    item['gender'] = 'women'
                else:
                    item['gender'] = None
                item['age'] = qiushi.css('.author>div::text').extract_first()
                item['zan_number'] = qiushi.css('.stats>.stats-vote>.number::text').extract_first()
                item['commit_number'] = qiushi.css('.stats-comments>a>.number::text').extract_first()
                item['commit_content'] = qiushi.css('.main-text::text').extract_first()
                image_url = qiushi.css('.thumb>a>img::attr(src)').extract_first()
                if image_url:
                    item['image'] = 'http:' + image_url
                else:
                    item['image'] = None
                yield item
            except TypeError:
                pass
    
        next = response.css('.pagination>li:last-child>a::attr(href)').extract_first()
        yield Request(self.start_url+next,self.parse )
