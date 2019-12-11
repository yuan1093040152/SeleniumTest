#coding=utf-8
from selenium import webdriver
import time,json

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.qidian.com/finish')
time.sleep(2)
source = driver.page_source
print (source)