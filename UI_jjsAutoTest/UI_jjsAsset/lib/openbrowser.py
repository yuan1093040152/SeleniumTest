#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/3 20:56
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time,unittest

 #判断运行浏览器
def open_browser(browser,url):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    else:
        pass
    driver.get(url)
    return driver


#封装元素操作
class testname:
    #打开浏览器
    def __init__(self,browser,url):
        self.browser = open_browser(browser,url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(30)

    #输入
    def ImputElement(self,type,element,value):
        self.browser.find_element(by=type, value=element).send_keys(value)

    #清除
    def CleanElement(self,type,element):
        self.browser.find_element(by=type,value=element).clear()


    #点击
    def ClickElement(self,type,element):
        self.browser.find_element(by=type,value=element).click()

    #新开页签
    def execute(self,js):
        self.browser.execute_script(js)
        self.browser.switch_to.window(self.browser.window_handles[-1])

    #获取文本信息
    # def getTextElement(self,type,element):
    #     self.browser.find_element_by_xpath(element).text
        #self.browser.find_element(by=type,value=element).text()

    #关闭窗口
    def Close(self):
        self.browser.close()

    #关闭浏览器
    def Quit(self):
        self.browser.quit()

    #时间
    def Time(self,s):
        time.sleep(s)

    #等待
    def Wait(self,s):
        self.browser.implicitly_wait(s)

    #校验
    def Expect(self,first,second):
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')
        if first == second:
            pass
        else:
            imagepath = './errorimage/%s-image.png' %nowtime
            self.browser.get_screenshot_as_file(imagepath)
            print('执行失败，截图文件名为：%s'%imagepath)

    #截图
    def Cutimage(self):
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')
        imagepath = './errorimage/%s-image.png' % nowtime
        self.browser.get_screenshot_as_file(imagepath)
        print('执行失败，截图文件名为：%s' % imagepath)