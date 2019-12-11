# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TailuSpiderMiddleware(object):
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


class TailuDownloaderMiddleware(object):
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

from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class SeleniumMiddleware():
    
    print ('正在调用SeleniumMiddleware类')
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def __del__(self):
        self.driver.quit()
        
    def process_request(self,request,spider):
        start_city = request.meta.get('start_city','深圳')
        end_city = request.meta.get('end_city','孝感')
        try:
            self.driver.get(request.url)
            self.driver.find_element_by_id('fromStationText').click()
            self.driver.find_element_by_id('fromStationText').send_keys(start_city)
            print ('已完成输入')
            time.sleep(1)
            self.driver.find_element_by_class_name('citylineover').click()
            self.driver.find_element_by_id('toStationText').click()
            self.driver.find_element_by_id('toStationText').send_keys(end_city)
            print ('已完成输入')
            time.sleep(1)
            self.driver.find_element_by_class_name('citylineover').click()
            self.driver.find_element_by_name('leftTicketDTO.train_date').click()
            self.driver.find_element_by_xpath('/html/body/div[30]/div[1]/div[2]/div[8]/div').click()
            self.driver.find_element_by_id('query_ticket').click()
            time.sleep(2)
            elems = self.driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr/td[5]')
            for elem in elems:
                for i in range(5):
                    elem.click()
                    rwid = elem.get_attribute('id')
                    priceid = u'price_' + rwid[3:]
                    xpath = '//tr[@id="%s"]/td'%priceid
                    try:
                        self.driver.implicitly_wait(0.5)
                        self.driver.find_element_by_xpath(xpath)
                        break
                    except NoSuchElementException:
                        pass
                    if i >= 5:
                        break`
                time.sleep(3)
            time.sleep(2)
            source = self.driver.page_source
            return HtmlResponse(url=request.url,body=source,request=request,encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)
            
    
    
    
    
    
    
    
    
    
    
    
    
