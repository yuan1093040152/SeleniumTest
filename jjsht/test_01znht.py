#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/21 11:12
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

https://www.cnblogs.com/denise1108/p/10339068.html
"""

from selenium.webdriver.common.by import By
from jjsht import htmain
import time,unittest


class ht_testcase(unittest.TestCase):
    url = 'http://itest.leyoujia.com/jjslogin/tologin'
    browser = 'Chrome'
    empno = '000012'
    password = '1'
    nowtime = time.strftime('%Y-%m-%d-%H-%M-%S')

    @classmethod
    def setUpClass(cls):  # 必须使用 @ classmethod装饰器, 所有test运行之前运行一次
        print('-----------开始智能合同web自动化巡检--------------')

    @classmethod
    def tearDownClass(cls):  # 必须使用 @ classmethod装饰器, 所有test运行结束后运行一次
        print('-----------结束智能合同web自动化巡检--------------')


    def setUp(self):  # 每条用例执行之前都会先执行它
        print('开始执行用例')

    def tearDown(self):  # 每条用例执行之后都会执行它
        print('结束执行用例')


    def test_ht001(self):
        '''进入智能合同'''
        print('开始执行用例：进入智能合同')
        passinfo = '智能合同管理列表'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        first = p.browser.find_element_by_xpath('//*[@id="main-content"]/div/div/div[1]/a[1]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht002(self):
        '''智能合同列表通过编号搜索'''
        print('开始执行用例：智能合同列表通过编号搜索')
        passinfo = '二手房买卖及居间服务合同'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME,'htNumber','MM-0001')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht003(self):
        '''智能合同列表通过合同名称搜索'''
        print('开始执行用例：智能合同列表通过合同名称搜索')
        passinfo = '二手房买卖及居间服务合同'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME, 'htName', '二手房买卖及居间服务合同')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht004(self):
        '''智能合同列表通过业务类型搜索'''
        print('开始执行用例：智能合同列表通过业务类型搜索')
        passinfo = '二手买卖'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.combo-input.text-input')
        p.Time(1)
        p.ClickElement(By.XPATH, '//*[@id="searchForm"]/div[3]/div/ul/li[3]')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[4]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht005(self):
        '''智能合同列表通过组合搜索'''
        print('开始执行用例：智能合同列表通过组合搜索')
        passinfo = '二手房买卖及居间服务合同'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ImputElement(By.NAME, 'htNumber', 'MM-0001')
        p.Time(1)
        p.ImputElement(By.NAME, 'htName', '二手房买卖及居间服务合同')
        p.Time(1)
        p.ClickElement(By.CSS_SELECTOR,'.combo-input.text-input')
        p.Time(1)
        p.ClickElement(By.XPATH, '//*[@id="searchForm"]/div[3]/div/ul/li[3]')
        p.ClickElement(By.XPATH,'//*[@id="searchBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[3]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht006(self):
        '''智能合同列表搜索点击重置'''
        print('开始执行用例：智能合同列表搜索点击重置')
        passinfo = '二手买卖'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.XPATH,'//*[@id="resetBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="data_list_content"]/tr/td[4]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht007(self):
        '''进入创建智能合同页面1'''
        print('开始执行用例：进入创建智能合同页面1')
        passinfo = '创建'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.btn.btn-primary.fr')#点击创建智能合同按钮
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="createButton"]').text
        print('获取需要校验的数据为：', first)
        print('正确的数据为：', passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

    def test_ht008(self):
        '''进入创建智能合同页面1点击取消'''
        print('开始执行用例：进入创建智能合同页面1点击取消')
        passinfo = '业务类型'
        p = htmain.testname(self.browser,self.url)
        p.get_znht(self.empno,self.password)
        p.ClickElement(By.CSS_SELECTOR,'.btn.btn-primary.fr')#点击创建智能合同按钮
        p.Time(2)
        p.ClickElement(By.XPATH,'//*[@id="backBtn"]')
        p.Time(2)
        first = p.browser.find_element_by_xpath('//*[@id="orderTablePeople"]/thead/tr/td[4]').text
        print('获取需要校验的数据为：',first)
        print('正确的数据为：',passinfo)
        # 校验
        if first == passinfo:
            print('执行通过，数据正确')
            pass
        else:
            p.Cutimage()
            self.assertEqual(first, passinfo, msg='执行失败，数据错误')
        p.Time(2)
        p.Close()
        p.Quit()

