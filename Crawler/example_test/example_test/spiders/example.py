# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import requests,json
import re,time
from example_test.items import ExampleItem 

class ExampleSpider(Spider):
    name = 'example'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']
    start_url = 'http://example.webscraping.com'
                
    
    def start_requests(self):
        yield Request(url=self.start_url,callback=self.parse_country,meta={'download_timeout':10},dont_filter=True)

        
    def parse_country(self, response):
        urls = response.css('#results>table>tr>td>div>a')
        urls = response.css('#results>table>tr>td>div>a::attr(href)').extract()
        for url in urls:
            yield Request(url=self.start_url + url,callback=self.parse_index,meta={'download_timeout':10},dont_filter=True)
        next_urls = response.css('#pagination>a::attr(href)').extract()
        yield Request(url=self.start_url + next_urls[-1],callback=self.parse_country,meta={'download_timeout':10},dont_filter=True)
    
    def parse_index(self,response):
        item = ExampleItem()
        item['National_flag'] = self.start_url + response.css('#places_national_flag__row>td>img::attr(src)').extract_first()
        item['Area'] = response.css('#places_area__row>.w2p_fw::text').extract_first()
        item['Population'] = response.css('#places_population__row>.w2p_fw::text').extract_first()
        item['Iso'] = response.css('#places_iso__row>.w2p_fw::text').extract_first()
        item['Country'] = response.css('#places_country__row>.w2p_fw::text').extract_first()
        item['Capital'] = response.css('#places_capital__row>.w2p_fw::text').extract_first()
        item['Continent'] = response.css('#places_tld__row>.w2p_fw::text').extract_first()
        item['Tld'] = response.css('#places_tld__row>.w2p_fw::text').extract_first()
        item['Currency_code'] = response.css('#places_currency_code__row>.w2p_fw::text').extract_first()
        item['Currency_name'] = response.css('#places_currency_name__row>.w2p_fw::text').extract_first()
        item['Phone'] = response.css('#places_phone__row>.w2p_fw::text').extract_first()
        item['Postal_code_format'] = response.css('#places_postal_code_format__row>.w2p_fw::text').extract_first()
        item['Postal_code_regex'] = response.css('#places_postal_code_regex__row>.w2p_fw::text').extract_first()
        item['Languages'] = response.css('#places_languages__row>.w2p_fw::text').extract_first()
        item['Neighbours'] = response.css('#places_neighbours__row>.w2p_fw::text').extract_first()
        yield item
        















