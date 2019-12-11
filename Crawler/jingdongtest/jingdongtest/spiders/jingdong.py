# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from jingdongtest.items import JingdongItem
from urllib.parse import quote

class JingdongSpider(Spider):
    name = 'jingdong'
    allowed_domains = ['www.jingdong.com']
    start_urls = ['http://www.jingdong.com/']
    seen_url = 'https://search.jd.com/Search?keyword='
    start_url = 'https://search.jd.com/Search?keyword={keyword}&enc=utf-8&page={page}'
    

 

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                url = self.seen_url + quote(keyword)
                print (url)
                yield Request(url = self.start_url.format(keyword=quote(keyword),page=page),callback=self.parse,meta={'page':page},dont_filter=True)


    def parse(self, response):
        print (response.text)
        item = JingdongItem()
        products = response.css('#J_goodsList>.gl-warp>.gl-item')
        print (len(products))
        for product in products:
            item['image'] = product.xpath('//img/@src').extract_first()
            item['details'] = product.css('.p-img>a::attr(href)').extract_first()
            item['name'] = product.css('.p-name>a>em::text').extract_first()
            item['price'] = product.css('.p-price>strong>i::text').extract_first()
            item['sales'] = product.css('.p-commit>strong>a::text').extract_first()
            item['shop'] = product.css('.J_im_icon>a::text').extract_first()
            item['tags'] = product.css('.p-icons>.goods-icons::text').extract()
            yield item




















