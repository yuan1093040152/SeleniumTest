#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/18 13:54
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
from selenium import webdriver
import time


def open_browser(browser,url):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        pass
    driver.get(url)
    return driver

class testname():

    def __init__(self,browser,url):
        self.browser = open_browser(browser,url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(30)

        self.id = 'id'
        self.xpath = 'xpath'
        self.link_text = "link text"
        self.partial_link_text = "partial link text"
        self.name = "name"
        self.tag_name = "tag name"
        self.class_name = "class name"
        self.css_selector = "css selector"


    def send_id(self,element,value):
        self.browser.find_element(self.id,element).send_keys(value)

    def send_name(self,element,value):
        self.browser.find_element(self.name,element).send_keys(value)


    def close(self):
        self.browser.close()


    def quit(self):
        self.browser.quit()


url = 'https://www.baidu.com/'
browser = 'Chrome'

p = testname(browser,url)

print('11')
time.sleep(1)

# p.send_id('kw','123')
# print('22')
# time.sleep(1)

p.send_name('wd','1234')
time.sleep(1)

p.close()
print('33')

p.quit()
print('44')

