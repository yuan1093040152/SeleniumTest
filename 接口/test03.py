#coding=utf-8

from selenium import webdriver
import time

#利用cookies实现自动登录

url = 'https://i.leyoujia.com/jjslogin/index'
driver = webdriver.Chrome()
driver.get('https://i.leyoujia.com/jjslogin/')
time.sleep(3)

#手动添加cookies
driver.add_cookie({'name':'JSESSIONID','value':'E7710B218E39D00FB353C5F2DBCFAA91','domain':'.leyoujia.com','path':'/','Expires':'','httpOnly':False,'HostOnly':False,'Secure':False})
driver.add_cookie({'name':'SESSION','value':'ZmZmNDMyZjItODAzMS00MzM1LTk1NDgtNDZlNWM4NjFlM2I4','domain':'i.leyoujia.com','path':'/','Expires':'','httpOnly':False,'HostOnly':False,'Secure':False})

time.sleep(3)
driver.get('https://i.leyoujia.com/jjslogin/index')
time.sleep(3)