# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement

def login(url,name):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element_by_name("userName").send_keys(name)
    driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
    driver.find_element_by_id("password").send_keys("1")
    driver.find_element_by_id("login_button").click()
    time.sleep(3)
    # driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/a').click()
    # time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="header-menu"]/li[3]/a').click()
    # time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="zhiyin-12"]/div[2]/a[1]/img').click()
    # driver.refresh()
    # time.sleep(2)
    # driver.find_element_by_xpath('//*[@id="main-content"]/div[2]/div/div[1]/a[2]').click()
    # driver.find_element_by_xpath('//*[@id="myProjectForm"]/div[1]/div[2]/button[1]').click()
    # time.sleep(3)
    # a = driver.find_element_by_xpath('//*[@id="myProject-list-table"]/tr[1]/td[9]').text
    # if a == u'代理中':
    #     print ('ok')
    # else:
    #     print ('NO')
    # driver.quit()

def main ():
    url = 'http://172.16.22.100/jjslogin/index'
    name = u'周棵'
    login(url,name)

if __name__ == "__main__":
    main()
