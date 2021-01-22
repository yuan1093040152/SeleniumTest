#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/21 11:36
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import unittest #导入unittest


def calc(a,b):
    return a/b

class TestCalc(unittest.TestCase): # 继承unittest.TestCase

    @classmethod
    def setUpClass(cls): #必须使用 @ classmethod装饰器, 所有test运行之前运行一次
        print('我是setupClass')

    @classmethod
    def tearDownClass(cls): #必须使用 @ classmethod装饰器, 所有test运行结束后运行一次
        print('我是tearDownClass')

    def setUp(self):#每条用例执行之前都会先执行它
        print('我是setup')

    def tearDown(self):#每条用例执行之后都会执行它
        print('我是teardown')

    def test_calc1(self): #下面的三引号/双引号中显示的是描述信息
        '''测试正常的'''
        # result = calc(2,1)
        # self.assertEqual(2,result,'除法运算不正确')
        print('calc1')

    def test_calc2(self):
        print('calc2')
        "测试异常的"
        # result = calc(2, 2)
        # self.assertEqual(1,2,'结果不正确')

    def test_mysql(self):
        '''测试mysql'''
        print('test_mysql')

    def test_login(self):
        '''测试登录'''
        print('print test_login')

    def test_abc(self):
        print('abc')

    def test_zbc(self):
        print('zbc')

    def test_fail(self):
        self.assertEqual(1,2,msg='测试失败的') #msg表示如果代码执行失败，则打印的信息

unittest.main() #运行当前文件里面的所有测试用例
#执行顺序：执行所有以test开头的方法/用例，且按照方法/用例名称A-Z顺序执行，而不是按照书写顺序