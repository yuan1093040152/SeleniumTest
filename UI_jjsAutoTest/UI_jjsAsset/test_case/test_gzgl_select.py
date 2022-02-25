#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/2/25 17:11
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


from UI_jjsAutoTest.UI_jjsAsset.lib.rerun import TestCase_
from UI_jjsAutoTest.UI_jjsAsset.page.gz_page import gzgl
import unittest


class jggl_select(TestCase_):

    @classmethod
    def setUpClass(self):  # 必须使用 @ classmethod装饰器, 所有test运行之前运行一次
        print('-----------开始盖章申请UI自动化巡检--------------')
        self.gzgl = gzgl()
        self.gzgl.url()
        self.gzgl.max_window()
        self.gzgl.itestlogin()



    @classmethod
    def tearDownClass(self):  # 必须使用 @ classmethod装饰器, 所有test运行结束后运行一次
        print('-----------结束盖章申请UI自动化巡检--------------')
        self.gzgl.close_page()
        self.gzgl.quit_page()


    def test_open_gz_gdbb(self):
        """打开固定版本盖章申请页面"""
        self.gzgl.open_gz_gdbb_url()
        assert (self.gzgl.gz_gdbb_url_check(),'固定版本盖章')


    def test_open_gz_dpgzh(self):
        """打开店铺告知函盖章申请"""
        self.gzgl.open_gz_dpgzh_url()
        assert (self.gzgl.gz_dpgzh_url_check(),'店铺告知函盖章申请')


    def test_open_gz_srzm(self):
        """打开收入证明盖章"""
        self.gzgl.open_gz_srzm_url()
        assert (self.gzgl.gz_srzm_url_check(),'收入证明盖章')


    def test_open_gz_ryzs(self):
        """打开荣誉证书盖章"""
        self.gzgl.open_gz_ryzs_url()
        assert (self.gzgl.gz_ryzs_url_check(),'荣誉证书盖章')


    def test_open_gz_jzwc(self):
        """打开借章外出申请"""
        self.gzgl.open_gz_jzwc_url()
        assert (self.gzgl.gz_jzwc_url_check(),'借章外出申请')


    def test_open_gz_xmjyb(self):
        """打开项目结佣表/结算表盖章"""
        self.gzgl.open_gz_xmjyb_url()
        assert (self.gzgl.gz_xmjyb_url_check(),'项目结佣表/结算表盖章')


    def test_open_gz_cgh(self):
        """打开催告函盖章"""
        self.gzgl.open_gz_cgh_url()
        assert (self.gzgl.gz_cgh_url_check(),'催告函盖章')


    def test_open_gz_qt(self):
        """打开其他盖章"""
        self.gzgl.open_gz_qt_url()
        assert (self.gzgl.gz_qt_url_check(),'其他盖章')


    def test_open_gz_zlbaht(self):
        """打开租赁备案合同"""
        self.gzgl.open_gz_zlbaht_url()
        assert (self.gzgl.gz_zlbaht_url_check(),'租赁备案合同')


    def test_open_gz_wfba(self):
        """打开无法备案"""
        self.gzgl.open_gz_wfba_url()
        assert (self.gzgl.gz_wfba_url_check(),'无法备案')


    def test_open_gz_cght(self):
        """打开采购合同"""
        self.gzgl.open_gz_cght_url()
        assert (self.gzgl.gz_cght_url_check(),'采购合同')