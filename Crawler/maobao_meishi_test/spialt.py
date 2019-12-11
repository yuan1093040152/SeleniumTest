#coding=utf-8
'''
Created on 2018年7月16日

@author: kai.yangf
'''

from selenium import webdriver
import requests,json,time,re
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

def search(keyvalue):
    driver.get('https://www.taobao.com/')
    driver.implicitly_wait(20)
    driver.find_element_by_id('q').send_keys(keyvalue)
    driver.find_element_by_class_name('btn-search').click()
    time.sleep(1)
    get_products()
    totalText = driver.find_element_by_class_name('total').text
    pattern = re.compile('(\d+)')
    total = int(re.search(pattern, totalText).group(1))
    return total
    
def page_skip(page_number):
    driver.find_element_by_css_selector('.form>.input.J_Input').clear()
    driver.find_element_by_css_selector('.form>.input.J_Input').send_keys(page_number)
    driver.find_element_by_css_selector('.btn.J_Submit').click()
    time.sleep(0.5)
    get_products()



def get_products():
    html = driver.page_source
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    i = 0
    for item in items:
        print (item)
        product = {
                   'image' : item.find('.pic .img').attr('src'),
                   'price' : item.find('.price').text(),
                   'deal'  : item.find('.deal-cnt').text(),
                   'title' : item.find('.title').text(),
                   'shop'  : item.find('.shop').text(),
                   'location'  : item.find('.location').text(),
                   }
        print (product)
#         print (item)
        i += 1
    print ('current page: ',i)


def main():
    keyvalue = u'美食'
    total = search(keyvalue)
#     for page_number in range(2,total+1):
#         page_skip(page_number)
#     driver.quit()
    

if __name__ == '__main__':
    main()

