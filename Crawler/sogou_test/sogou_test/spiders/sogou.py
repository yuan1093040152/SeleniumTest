# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from sogou_test.items import SogouItem

class SogouSpider(Spider):
    name = 'sogou'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['http://weixin.sogou.com/']
    start_url = 'http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page='
    print ('进入SogouSpider')

    def start_requests(self):
        print ('进入start_requests')
        for page in range(1,self.settings.get('MAXPAGE')+1):
            yield Request(url=self.start_url + str(page),callback=self.parse_page,meta={'download_timeout':10},dont_filter=True)

    

    def parse_page(self, response):
        page_urls = response.css('.news-box>.news-list>li>.txt-box>h3>a::attr(href)').extract()
        for page_url in page_urls:
            yield Request(url=page_url,callback=self.parse_index,meta={'download_timeout':10},dont_filter=True)
     
    def parse_index(self,response):
        print ('进入页面')
        item = SogouItem()
        item['activity_name'] = response.css('#activity-name::text').extract_first()
        item['meta_content'] = response.css('.rich_media_meta_text::text').extract_first()
        item['js_name'] = response.css('#js_name::text').extract_first()
        item['date'] = response.css('#publish_time::text').extract_first()
        essays = response.css('#js_content>p>span::text').extract()
        item['essay'] = ''
        for essay in essays:
            item['essay'] += essay
        yield item
          

            