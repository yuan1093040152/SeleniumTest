# coding=utf-8
from selenium import webdriver
import time

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

    # 将页面滚动条拖动至底部
    # js = 'var q=document.documentElement.scrollTop=10000'
    # lower = driver.execute_script(js)
    # time.sleep(3)

    # # 将页面滚动条拖动至底部
    # js1 = 'var q=document.documentElement.scrollTop=0'
    # up = driver.execute_script(js1)
    # time.sleep(3)

    driver.quit()

# def main ():
#     url = 'http://172.16.22.100/jjslogin/index'
#     name = u'周棵'
#     login(url,name)
#
# if __name__ == "__main__":
#     main()


# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def open_browser(name, url):
    if name == 'chrome':
        browser = webdriver.Chrome()
    elif name == 'firefox':
        browser = webdriver.Firefox()
    browser.get(url)
    return browser


class UI_init():



    def __init__(self,name,url):
        self.browser = open_browser(name,url) #http://172.16.22.100/jjslogin/tologin
        time.sleep(3)


    def imput_text(self,type,value,text):
        self.browser.find_element(by=type,value=value).send_keys(text)
        time.sleep(2)
#        browser.find_element(by=type,value=value).send_keys(text)
#    browser.find_element_by_xpath("//input[@id='workerStr']").send_keys(u"周棵")
#    browser.find_element_by_xpath("//*[@href='javascript:;']").click()
#    browser.find_element_by_xpath("//input[@id='password']").send_keys('123456')

    def click_element(self,type,value):
        self.browser.find_element(by=type,value=value).click()
#    browser.find_element_by_id('login_button').click()

    def browser_quit(self):
        self.browser.quit()

Ui = UI_init('chrome','http://www.baidu.com')
Ui.imput_text(By.ID,'kw',u'吃吃吃')
Ui.click_element(By.ID,'su')
Ui.browser_quit()


