#coding=utf-8
'''
Created on 2018年7月22日

@author: kai.yangf
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import requests
def ipporxy():
    response = requests.get('http://123.207.35.36:5010/get/')
    proxy = response.text
    return proxy

# proxy = ipporxy()
# for i in range(100):
#     # response = requests.get('http://www.httpbin.org/get')
#     flag = True
#     number = 0
#     while flag:
#         try:
#             proxies = { "http": proxy, "https": proxy, }  
#             response = requests.get("http://example.webscraping.com", proxies=proxies,timeout=5) 
#             if response.status_code == 200:
#                 value = 'i:%d , number:%d , status:%d'%(i,number,response.status_code)
#                 print (value)
#                 break
#         except Exception as e:
#             proxy = ipporxy()
#             number += 1
#         if number >= 5:
#             break
#         
proxy = '204.48.31.200:8080'

proxies = { "http": proxy, "https": proxy, }  
response = requests.get("http://example.webscraping.com", proxies=proxies,timeout=5) 
print (response.text)