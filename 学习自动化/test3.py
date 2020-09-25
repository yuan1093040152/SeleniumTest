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
    driver.find_element_by_xpath('/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/a').click()
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

def main ():
    url = 'http://172.16.22.100/jjslogin/index'
    name = u'周棵'
    login(url,name)

if __name__ == "__main__":
    main()
