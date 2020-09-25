# coding=utf-8
from selenium import webdriver
import time


def login():
    driver = webdriver.Chrome()
    url = "http://www.baidu.com"
    driver.get(url)
    driver.maximize_window()
    # time.sleep(10)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='kw']").send_keys(u'python')
    driver.find_element_by_id('su').click()
    time.sleep(2)

    # 将页面滚动条拖动至底部
    js = 'var q=document.documentElement.scrollTop=10000'
    lower = driver.execute_script(js)
    time.sleep(3)

    # 将页面滚动条拖动至底部
    js1 = 'var q=document.documentElement.scrollTop=0'
    up = driver.execute_script(js1)
    time.sleep(3)

    driver.quit()

print('234')
login()