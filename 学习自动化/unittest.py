#coding=utf-8
from selenium import webdriver
import time,unittest
import HTMLTestRunner

class login(unittest.TestCase):
    def setUp(self):               #开始执行前需要做的事（每条用例都会执行）
        print (u'开始执行')
        self.driver = webdriver.Chrome()
        self.driver.get('http://172.16.3.100/jjslogin/index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):          #执行用例结束后需要做的事情（没条用例都会执行）
        print (u'已执行完')
        self.driver.close()

    def test_haha(self):       #用例1
        self.driver.find_element_by_name("userName").send_keys( u'吴磊')
        self.driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
        self.driver.find_element_by_id("password").send_keys("1")
        self.driver.find_element_by_id("login_button").click()
        time.sleep(3)
        exc = self.driver.find_element_by_xpath("//*[@id='topics']/div[1]/div/div/div[2]/span[2]/a").text
        print (u'登录人：' + exc)
        if exc == u'吴磊':
            print (u'登录成功')
        time.sleep(1)

    def test_huhu(self):  # 用例2
        self.driver.find_element_by_name("userName").send_keys(u'袁猛')
        self.driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
        self.driver.find_element_by_id("password").send_keys("1")
        self.driver.find_element_by_id("login_button").click()
        time.sleep(3)
        exc = self.driver.find_element_by_xpath("//*[@id='topics']/div[1]/div/div/div[2]/span[2]/a").text
        print (u'登录人：' + exc)
        if exc == u'袁猛':
            print (u'登录成功')
        time.sleep(1)

if __name__ == '__main__':    #直接执行该文件
    # unittest.main()
    test_suite = unittest.TestSuite()      # 创建一个测试集合
    # test_suite.addTest(MyTest('test_run1'))      # 测试套件中添加测试用例
    test_suite.addTest(unittest.makeSuite(login))     #使用makeSuite方法添加所有的测试方法
    fp = open('C:\\Users\\admin\\Desktop\\res.html', 'wb')    # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'测试用例执行情况')     # 生成执行用例的对象
    runner.run(test_suite)        # 执行测试套件
