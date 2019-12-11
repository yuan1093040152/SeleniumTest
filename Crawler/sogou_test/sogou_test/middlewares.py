# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class SogouTestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SogouTestDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import requests

class ProxyMiddleware(object):
    #动态设置ip代理
    PROXY_POOL_URL = 'http://123.207.35.36:5010/get/'
    proxy_ip = '204.48.31.200:8080'
    def process_request(self, request, spider):
#         url = request.url
#         write(url)
        request.meta["proxy"] = 'http://' +  self.proxy_ip
        print ('当前请求的ip: ',self.proxy_ip)
        return None
    
    def process_response(self,request, response, spider):  
        print ('当前请求返回status: ',response.status)
        if response.status != 200:
            proxy_ip = requests.get(self.PROXY_POOL_URL).text
            self.proxy_ip = proxy_ip
            print ('新请求的代理ip: ',self.proxy_ip)
            return request
        else:
            return response
            
    
    def process_exception(self,request, exception, spider):
        proxy_ip = requests.get(self.PROXY_POOL_URL).text
        self.proxy_ip = proxy_ip
        return request

from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException
class SeleniumMiddleware():
    
    print ('正在调用SeleniumMiddleware类')
    
    def __init__(self,cookies,service_args=[]):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page=1&ie=utf8')
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        time.sleep(2)
        self.driver.refresh()
            
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies = crawler.settings.get('COOKIES'),
        )
        
    def __del__(self):
        pass
#         self.driver.quit()
    
    def process_request(self,request,spider):
        print ('谷歌正在启动')
        page = request.meta.get('page',1)
        try:
            print ('request.url: ',request.url)
            self.driver.get(request.url)
            time.sleep(2)
            return HtmlResponse(url = request.url,body=self.driver.page_source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)








