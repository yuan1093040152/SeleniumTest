#coding=utf-8
'''
Created on 2018年3月17日

@author: 唐路
'''

import urllib2,urlparse
import time
import datetime
from _weakref import proxy
from link_crawler import Throttle
from public import *


class Tgrottle:
    
    def __init__(self,delay):
        self.delay = delay
        self.domains = {}
    
    def wait(self,url):
        domain = urlparse.urlparse(url).netloc
        last_accessed = self.domains.get(domain)
        
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            if sleep_secs > 0 :
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.datetime.now() 
        
        
        
def download(url,user = 'wswp',num = 2):
    print 'Download:',url
    headers = {'User-agent':user}
    request = urllib2.Request(url,headers = headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Error: ',e.reason
        html = None
        if num > 0:
            if hasattr(e,'code') and e.code >= 500:
                return download(url,num-1)
    return html


throttle = Throttle(1)
for i in range(100):
    url = 'http://example.webscraping.com'
    throttle.wait(url)
    result = download(url)
    write_txt(result)


