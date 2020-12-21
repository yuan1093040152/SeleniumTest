#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/18 11:57
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from selenium import webdriver
import time


url = 'https://www.baidu.com/'

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()



driver.find_element('id','kw').send_keys('123')

time.sleep(2)

driver.close()
driver.quit()