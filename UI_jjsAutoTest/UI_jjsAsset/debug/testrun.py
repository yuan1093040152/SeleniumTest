#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/22 16:52
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import time,os
import unittest

from BeautifulReport import BeautifulReport
from HTMLTestRunner import HTMLTestRunner
from UI_jjsAutoTest.UI_jjsAsset.test_case.test_jggl_select import jggl_select
from UI_jjsAutoTest.UI_jjsAsset.lib.path import mainpath,test_case_path,report_path



if __name__ == '__main__':


    testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件

    # 把测试用例加入到测试用力集合中去，将用例加入到检测套件中
    testunit.addTest(jggl_select("test_jump_tzbg"))
    testunit.addTest(jggl_select("test_jump_htgl"))
    testunit.addTest(jggl_select("test_jump_sdfgl"))
    testunit.addTest(jggl_select("test_jump_zzgl"))

    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    filename = report_path + os.path.sep + now + 'report.html'
    f = open(filename, 'wb')
    runner = HTMLTestRunner(f, verbosity=2, title="Testcase Report", description=u'用例执行情况：')
    runner.run(testunit)
    f.flush()
    f.close()
    print('测试报告已生成，路径：%s' % filename)






    #runner = BeautifulReport(testunit)#运行找到的所有用例
    #file_name = '%s-testreport.html' % now  # 报告文件名
    #filename = report_path + os.path.sep
    # runner = BeautifulReport(f,title="Testcase Report", description="测试用例明细")
    #runner.report('自动化测试报告', filename=file_name, report_dir=filename)
    # print('测试报告已生成，路径：%s' % filename)