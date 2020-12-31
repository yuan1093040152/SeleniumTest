#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/17 17:57
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests
import eventlet
import time
from selenium import webdriver

a = ['123','234']
for i in a:
    print(i)


i = 'http://172.16.22.100/jjsht/fddThird/gotoSignPage/97e231ab-9c10-4001-b33e-b316e17f7bb8/71bf861b-797c-4b6f-9d84-fbceb7ce9377'

driver = webdriver.Chrome()

driver.get(i)
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(1)
driver.switch_to.frame('myiframe')
driver.find_element_by_id('confirmSubmit').click()
time.sleep(1)
driver.find_element_by_id('smsval').send_keys('999999')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="smspanel"]/div/div/div/a[1]').click()

time.sleep(5)
print('合同签署完成')
driver.close()
driver.quit()







