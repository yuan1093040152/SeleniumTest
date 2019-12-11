#coding=utf-8
'''
Created on 2018年3月19日

@author: 唐路
'''
import re


url = 'http://example.webscra^ping.com/places/default/view/China-47'
url = re.sub('[^/0-9a-zA-Z\-,.;_]','_',url)
url = re.sub('[^0-9]','_',url)
print url






import urlparse
url = 'http://example.webscraping.com/index'
url = 'https://www.baidu.com/s?ie=utf-8'
components = urlparse.urlsplit(url)
print components
print components.path
path = components.path
if not path:
    path = '/index.html'
elif path.endswith('/'):
    path += 'index.html'

    

