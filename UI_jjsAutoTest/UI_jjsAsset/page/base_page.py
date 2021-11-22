#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 14:20
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


from UI_jjsAutoTest.UI_jjsAsset.lib.base import Base
from UI_jjsAutoTest.UI_jjsAsset.lib.path import BASE_URL
from UI_jjsAutoTest.UI_jjsAsset.lib.operation_mysql import MysqlServer
from UI_jjsAutoTest.UI_jjsAsset.lib import read_config


class BasePage(object):
    def __init__(self):
        self.d = Base('chrome')
        self.m = MysqlServer()
        self.itestempno = read_config.read_config('user', 'itestempno')
        self.iempno = read_config.read_config('user', 'iempno')
        self.itestpassword = read_config.read_config('user', 'itestpassword')
        self.ipassword = read_config.read_config('user', 'ipassword')
        self.browser = read_config.read_config('browser', 'browser')
        self.itesturl = read_config.read_config('url', 'itesturl')
        self.iurl = read_config.read_config('url', 'iurl')
        self.jgurl = read_config.read_config('url', 'jgurl')
        self.jgxqurl = read_config.read_config('url','jgxqurl')


    def url(self):
        self.d.open(self.itesturl)

    def quit(self):
        self.d.quit()

    def max_window(self):
        self.d.max_window()

    # 关闭网页
    def close_page(self):
        self.d.close()

