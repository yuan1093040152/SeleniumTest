#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 16:04
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
from UI_jjsAutoTest.UI_jjsAsset.page.login_page import LoginPage


class aa(LoginPage):

    def bb(self):
        self.url()
        self.itestlogin()
        self.quit()


test = aa().bb()