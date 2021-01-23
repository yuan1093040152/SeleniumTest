#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/21 13:40
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import unittest,HTMLTestRunner,time,BeautifulReport

# case_path = "../jjsht"
case_path = "E:/SeleniumTest/jjsht"

# suite = unittest.TestSuite()#创建测试套件
# all_cases = unittest.defaultTestLoader.discover(case_path,pattern='test_*.py')
# #找到某个目录下所有的以test开头的Python文件里面的测试用例
# for case in all_cases:
#     suite.addTests(case)#把所有的测试用例添加进来
# fp = open('./htmllog/'+now+'res.html','wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='all_tests',description='所有测试情况')
# #运行测试
# runner.run(suite)

tests = unittest.defaultTestLoader.discover(case_path,'test_*.py') #找指定路径下以.py结尾的文件
runner = BeautifulReport.BeautifulReport(tests)#运行找到的所有用例
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
file_name = '%s-report.html'%now #报告文件名
runner.report('自动化测试报告',filename=file_name,report_dir='./htmllog/')#产生报告
