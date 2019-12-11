#coding=utf-8
'''
Created on 2018年7月21日

@author: kai.yangf
'''
import pymongo


client = pymongo.MongoClient('127.0.0.1')
db = client.qidian
connect = db.finish
 
names = db.get_collection('finish')
print (names)
namelist =  connect.find({},{'classes':1})
names = []
for name in namelist:
    names.append(name["classes"])

area_index = list(set(names))
area_index.reverse()
area_count = []
for index in area_index:
    area_count.append(names.count(index))


       # step 1
from pyecharts import Bar, Scatter3D
from pyecharts import Page

bar = Bar("猫眼评分不完全数据统计")
bar.add("评分", area_index, area_count, is_stack=True)
       # step 2
 
 
 
 
bar.render()        # step 3