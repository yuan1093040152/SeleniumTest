#coding=utf-8
'''
Created on 2018年7月21日

@author: kai.yangf
'''
import pymongo
from pymongo.mongo_client import MongoClient


client = MongoClient('127.0.0.1',27017)
db = client.test

storage = db.maoyanTop100
