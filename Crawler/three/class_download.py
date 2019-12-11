#coding=utf-8
'''
Created on 2018年3月19日

@author: 唐路
'''
import urllib2,re
from public import *
import random
from DiskCache_3_2 import *



class Downlaoder():
    def __init__(self,delay=2,user_agent='wswp',proxies=None,num_retries=1,cache=DiskCache()):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache
        
    def __call__(self,url):
        result = None
        if self.cache:   #判断cache是否被定义
            try:
                result = self.cache[url]        #查看url是否访问过
            except KeyError:
                pass
            else:   
                if self.num_retries > 0 and 500 <= result['code'] <= 600:       #查看url是否之前访问报错
                    result = None
        if result is None:          #判断url是否有缓存
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None   
        headers = {'User-agenmt':self.user_agent}
        result = self.download(url,headers,proxy,self.num_retries)
        if self.cache:
            self.cache[url] = result
        return result['html']

    def download(self,url,headers,proxy,num_retries=2,data=None):
        print 'Downloading:',url
        request = urllib2.Request(url,headers = headers)
        opener = urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme:proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            response = opener.open(request)
            html = response.read()
            code = response.code
        except urllib2.URLError as e:
            print 'Error: ',e.reason
            html = None
            if num_retries > 0 and e.code >= 500:
                code = e.code
                return self.download(self,url,headers,proxy,num_retries-1,data)
            else:
                code = None
        return {'html':html,'code':code}
        