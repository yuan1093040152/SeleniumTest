#coding=utf-8
'''
Created on 2018年3月20日

@author: 唐路
'''

with open('G:\\Crawler\\log\\with.txt','rb') as fp:
    for link in fp:
        print  link.encode('utf-8')