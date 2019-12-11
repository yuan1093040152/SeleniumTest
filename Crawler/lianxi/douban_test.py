#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
import requests,re















# response = requests.get('https://book.douban.com/')
# content = response.text
# compile = re.compile('<li.*?>.*?cover">.*?<a.*?href="(.*?)".*?title="(.*?)".*?<div.*?author">(.*?)</div>.*?<span.*?year">(.*?)</span>',re.S)
# pettern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
# pettern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
# print (pettern)
# results = re.findall(pettern,content)
# print (len(results))
# for result in results:
#     print (result)


 
import requests 
import re 
content = requests.get('https://book.douban.com/').text 
# print (content)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S) 
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)" title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
# pattern = re.compile('href="(.*?)"')
results = re.findall(pattern, content) 
print(results) 
for result in results: 
    url, name, author, date = result 
    author = author.strip()
    date = date.strip()
    print (url, name, author,date)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     