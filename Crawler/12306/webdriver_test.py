#coding=utf-8
'''
Created on 2018年8月6日

@author: kai.yangf
'''
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


start_city = u'深圳'
end_city = u'岳阳'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(20)
driver.find_element_by_id('fromStationText').click()
driver.find_element_by_id('fromStationText').send_keys(start_city)
print ('已完成输入')
time.sleep(1)
driver.find_element_by_class_name('citylineover').click()
driver.find_element_by_id('toStationText').click()
driver.find_element_by_id('toStationText').send_keys(end_city)
print ('已完成输入')
time.sleep(1)
driver.find_element_by_class_name('citylineover').click()
driver.find_element_by_name('leftTicketDTO.train_date').click()
driver.find_element_by_xpath('/html/body/div[30]/div[1]/div[2]/div[8]/div').click()
driver.find_element_by_id('query_ticket').click()
time.sleep(2)
elems = driver.find_elements_by_xpath('//tbody[@id="queryLeftTable"]/tr/td[5]')
for elem in elems:
    for i in range(5):
        elem.click()
        rwid = elem.get_attribute('id')
        priceid = u'price_' + rwid[3:]
        xpath = '//tr[@id="%s"]/td'%priceid
        try:
            driver.implicitly_wait(0.5)
            driver.find_element_by_xpath(xpath)
            break
        except NoSuchElementException:
            pass
        if i >= 5:
            break
    time.sleep(3)
time.sleep(2)
source = driver.page_source
print (source)











