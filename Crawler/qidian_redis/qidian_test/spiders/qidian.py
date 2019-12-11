# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from qidian_test.items import QidianItem

class QidianSpider(Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = ['http://www.qidian.com/']
    start_url = 'https://www.qidian.com/finish?page='
    
    def start_requests(self):
        for page in range(1,self.settings.get('MAXPAGE') + 1):
            yield Request(self.start_url + str(page),self.parse)

    def parse(self, response):
        item = QidianItem()
        current_page = response.css('.lbf-pagination-current::text').extract_first()
        print ('当前爬取的页面: ',current_page)
        books = response.css('.all-img-list li')
        for book in books:
            item['name'] = book.css('.book-mid-info h4 a::text').extract_first()
            item['author'] = book.css('.author .name::text').extract_first()
            item['classes'] = book.css('p.author > a:nth-child(4)::text').extract_first()
            item['classes_details'] = book.css('p.author > a:nth-child(6)::text').extract_first()
            item['content'] = book.css('.intro::text').extract_first()
            item['image'] = 'http:' +  book.css('li .book-img-box a img::attr(src)').extract_first()
            item['size'] = book.css('.update span span::text').extract_first()
            yield item
        
