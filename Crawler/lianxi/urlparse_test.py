#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
from urllib.parse import urlparse,urlencode

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print (type(result))
print (result)

params = {'name':'yangkai','age':'23'}
base_url = 'https://www.yangkai.com'
url = base_url + urlencode(params)
print (url)
 
