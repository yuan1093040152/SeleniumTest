#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 14:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import os

# 定义文件路径

mainpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件拼接
CONFIG_PATH = mainpath + os.path.sep + 'config' + os.path.sep + 'config.ini'


#调试文件拼接
debug_path = mainpath + os.path.sep + 'debug'


#截图文件拼接
errorimage_path = mainpath + os.path.sep + 'errorimage'


#公共方法文件拼接
lib_path = mainpath + os.path.sep + 'lib'


#公共用例文件拼接
page_path = mainpath + os.path.sep + 'page'


#日志文件拼接
#log_path = mainpath + os.path.sep + 'log'


#测试报告文件拼接
report_path = mainpath + os.path.sep + 'report'


#测试用例文件拼接
test_case_path = mainpath + os.path.sep + 'test_case'

#日志文件拼接
LOGPATH = mainpath + os.path.sep + 'log' + os.path.sep
WEBLOGPATH = LOGPATH + 'server.log'

WEBPICTUREPATH = mainpath + os.path.sep + 'errorimage' + os.path.sep + 'picture' + os.path.sep
DELREPORTPATH = os.path.join(mainpath ,'report')

#驱动路径
DRIVER_PATH = mainpath + os.path.sep + 'chromedriver' + os.path.sep + 'chromedriver.exe'


BASE_URL = 'http://itest.leyoujia.com'



CASEDIR = 'test_case'

if __name__ == '__main__':

    print(CONFIG_PATH)