#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 16:44
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
from UI_jjsAutoTest.UI_jjsAsset.lib.rerun import TestCase_
from UI_jjsAutoTest.UI_jjsAsset.page.jggl_page import jggl
import unittest


class jggl_select(TestCase_):

    @classmethod
    def setUpClass(self):  # 必须使用 @ classmethod装饰器, 所有test运行之前运行一次
        print('-----------开始机构管理UI自动化巡检--------------')
        self.jggl = jggl()
        self.jggl.url()
        self.jggl.max_window()
        self.jggl.itestlogin()



    @classmethod
    def tearDownClass(self):  # 必须使用 @ classmethod装饰器, 所有test运行结束后运行一次
        print('-----------结束机构管理UI自动化巡检--------------')
        self.jggl.quit()


    def test_Property_type(self):
        """产权类型租赁查询"""
        self.jggl.open_url()
        self.jggl.Property_type()


