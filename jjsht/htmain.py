#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/21 11:00
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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
class testname():
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

    #当前时间
    def Nowtime(self):
        time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))



    #进入智能合同列表
    def get_znht(self,empno,password):
        self.browser.find_element(By.ID,'workerNo').clear()
        self.browser.find_element(By.ID, 'workerNo').send_keys(empno)
        self.browser.find_element(By.ID, 'password').send_keys(password)
        self.browser.find_element(By.ID, 'login_button').click()
        print('已登录新系统')
        self.browser.implicitly_wait(10)
        try:
            self.browser.find_element(By.CLASS_NAME, 'aui_close').click()
        except:
            print('没有弹窗跳过')
            pass
        time.sleep(2)
        # 鼠标移到悬停元素上
        ele = self.browser.find_element(By.XPATH, '//*[@href="/jjscj/index"]')
        ActionChains(self.browser).move_to_element(ele).perform()

        self.browser.find_element(By.XPATH, '//*[@href="/znht/ht/index"]').click()
        print('进入智能合同管理列表')
        self.browser.implicitly_wait(10)
        #切换页面
        all_handles = self.browser.window_handles
        for handle in all_handles:
            if handle != self.browser.current_window_handle:
                self.browser.switch_to_window(handle)
                break
        time.sleep(2)










