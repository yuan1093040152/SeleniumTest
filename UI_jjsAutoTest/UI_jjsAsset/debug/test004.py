#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/19 15:35
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class ZRTestCase(unittest.TestCase):
    def setUp(self):
        print('开始执行测试用例：')


    def test_01(self):
        print('测试用例1')

    def test_02(self):
        print('测试用例2')

    def tearDown(self):
        print('一条用例执行完成。')

if __name__ == '__main__':
    testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件
    testunit.addTest(ZRTestCase("test_01"))#把测试用例加入到测试用力集合中去，将用例加入到检测套件中
    testunit.addTest(ZRTestCase("test_02"))
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    dir = 'report.html'
    f = open(dir, "wb")  # "wb"新建或者打开一个二进制文件，写入执行完的数据
    runner = HTMLTestRunner(f,title="Testcase Report", description="测试用例明细")
    # 调用HTMLTestRunner类定义测试报告内容
    runner.run(testunit)  # 调用HTMLTestRunner类下面的run()方法运行用例套件
    f.flush()
    f.close()  # 关闭测试报告文件