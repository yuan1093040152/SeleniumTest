#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
from urllib import request,parse

# response = urllib.request.urlopen('https://www.python.org')
# print (response.status)
# print (response.getheaders())
# print (response.getheader('Server'))

# print (response.read().decode('utf-8'))


 
url = 'http://python.org/post'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'Host' : 'httpbin.org'
}

dict = {'name' : 'kai.yang'}

data = bytes(parse.urlencode(dict),encoding='utf8')

req = request.Request(url,data = data,headers=headers,method='POST')


response = request.urlopen(req)
print (response.read().decode('utf-8'))








