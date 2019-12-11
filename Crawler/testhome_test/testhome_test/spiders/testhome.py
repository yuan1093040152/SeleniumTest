# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from testhome_test.items import TesthomeItem
import re

class TesthomeSpider(Spider):
    name = 'testhome'
    allowed_domains = ['testerhome.com']
    start_urls = ['http://testerhome.com/']
    start_url = 'https://testerhome.com/seveniruby/followers'
    domain_url = 'https://testerhome.com'

    def start_requests(self):
        yield Request(self.start_url,self.parse_index)
    
    def parse_index(self, response):
        users = response.css('.col-md-8>.panel-default>.panel-body>.row>div')
        for user in users:
            username = user.css('.user-name::attr(href)').extract_first()
            yield Request(self.domain_url + username,self.parse_details )
            yield Request(self.domain_url + username + '/followers',self.parse_index )
            yield Request(self.domain_url + username + '/following',self.parse_index )

    
    def parse_details(self,response):
        item = TesthomeItem()
        item['name'] = response.css('div.media > div.media-body > div:nth-child(1)::text').extract_first().strip()
        ranking = response.css('.number::text').extract_first()
        item['ranking'] = re.search('(\d+)',ranking).group(1)
        item['date'] = response.css('.number>span::text').extract_first()
        company = response.css('.company::text').extract_first()
        if company:
            item['company'] = company[:-2].strip()
        else:
            item['company'] = None
        item['address'] = response.css('.company>span>a::text').extract_first()
        item['post'] = response.css('div.item.counts > span:nth-child(1)::text').extract_first()
        item['Respon'] = response.css('div.item.counts > span:nth-child(2)::text').extract_first()
        item['attention'] = response.css('.followers>.counter::text').extract_first()
        item['concerned'] = response.css('.following>.counter::text').extract_first()
        item['collect'] = response.css('.stars>.counter::text').extract_first()
        yield item