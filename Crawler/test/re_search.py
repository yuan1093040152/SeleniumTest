#coding=utf-8
'''
Created on 2018年3月18日

@author: 唐路
'''
import re

link = '/places/default/view/register'
link_regex = '/(index|view)'

if re.search(link_regex, link):
    print  True
else:
    print False