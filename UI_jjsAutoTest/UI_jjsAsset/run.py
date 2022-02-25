#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/12 14:37
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import unittest,time
from BeautifulReport import BeautifulReport
import os
import time
from UI_jjsAutoTest.UI_jjsAsset.config.readconfig import ReadConfig
from UI_jjsAutoTest.UI_jjsAsset.lib.path import mainpath,test_case_path,report_path
from UI_jjsAutoTest.UI_jjsAsset.lib.HTMLTestRunner import HTMLTestRunner
# from lib.sendemail import SendEmail
# from lib.download_driver import osSystem
from UI_jjsAutoTest.UI_jjsAsset.lib.tool import delreport
from UI_jjsAutoTest.UI_jjsAsset.lib.sendemall import SendEmail



local_readConfig = ReadConfig()
SendEmail = SendEmail()


class Main:
    def __init__(self):
        global title
        title = local_readConfig.get_project('title')
    def run(self):
        delreport()
        suite = unittest.TestSuite()

        cases = unittest.defaultTestLoader.discover(test_case_path)
        for case in cases:
            suite.addTest(case)
        now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        filename = report_path + os.path.sep + now +'report.html'
        f = open(filename ,'wb')
        runner = HTMLTestRunner(f,verbosity=2,title=u'%s'%title, description=u'用例执行情况：')
        runner.run(suite)
        f.flush()
        f.close()
        print('测试报告已生成，路径：%s'%filename)


        # 方法2
        # tests = unittest.defaultTestLoader.discover(test_case_path,pattern='test_gzgl*.py',top_level_dir=None) #找指定路径下以.py结尾的文件
        # runner = BeautifulReport(tests)#运行找到的所有用例
        # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        # filename = '%s-report.html'%now #报告文件名
        # runner.report('自动化测试报告',filename=filename,report_dir=report_path)#产生报告

        #发送邮件
        SendEmail.Email(file=filename)

if __name__ == '__main__':
    Main().run()
