# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from qfangwang_test.items import QfangwangItem

class QfangwangSpider(Spider):
    name = 'qfangwang'
    allowed_domains = ['shenzhen.qfang.com']
    start_urls = ['http://shenzhen.qfang.com/']
    start_url = 'https://{city}.qfang.com/sale/f{page}'
    
    def start_requests(self):
        citys = ['shenzhen','shanghai','qingdao','guangzhou','nanjing','zhuhai','beijing','dongguan','foshan','hangzhou','huizhou','huzhou','jiaxing','langfang','nanning','nantong','suzhou','dayuan','taicang','taiyuan','xianggang','xuzhou','zhuhai','zhongshan' ]
        citys = ['shenzhen']
        for city in citys:
            for page in range(1,self.settings.get('MAXPAGE')+1):
                yield Request(self.start_url.format(city=city,page=page),self.parse)
    
    
    
    def parse(self, response):
        item = QfangwangItem()
        rooms = response.css('.house-detail>ul>.clearfix')
        for room in rooms:
            item['image'] = room.css('.lazy::attr(src)').extract_first()
            item['title'] = room.css('.house-title>.showKeyword::text').extract_first()
            item['house'] = room.css('p.house-about.clearfix > span:nth-child(2)::text').extract_first()
            item['size'] = room.css('p.house-about.clearfix > span:nth-child(4)::text').extract_first()
            item['fitment'] = room.css('p.house-about.clearfix > span:nth-child(6)::text').extract_first()
            item['floor'] = room.css('p.house-about.clearfix > span:nth-child(8)::text').extract_first()
            item['orientation'] = room.css('p.house-about.clearfix > span:nth-child(10)::text').extract_first()
            item['year'] = room.css('p.house-about.clearfix > span:nth-child(12)::text').extract_first()
            item['district'] = room.css('span.whole-line > a:nth-child(1)::text').extract_first()
            item['location'] = room.css('span.whole-line > a:nth-child(2)::text').extract_first()
            item['estate'] = room.css('span.whole-line > a:nth-child(3)::text').extract_first()
            item['watch'] = room.css('.text::text').extract_first()
            item['tags'] = room.css('.house-traffic.clearfix>span::text').extract()
            item['tags'].append(room.css('.house-traffic.clearfix>a>span::text').extract_first())
            item['price'] = room.css('.sale-price::text').extract_first()
            item['unitprice'] = room.css('.show-price>p::text').extract_first()
            yield item







