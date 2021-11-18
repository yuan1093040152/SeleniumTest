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


    def test_Property_type_zl(self):
        """产权类型租赁查询"""
        self.jggl.open_url()
        self.jggl.Property_type_zl()
        assert(self.jggl.Property_type_check(),'租赁')


    def test_Property_type_zgwy(self):
        """产权类型自购物业查询"""
        self.jggl.open_url()
        self.jggl.Property_type_zgwy()
        assert(self.jggl.Property_type_check(),'自购物业')


    def test_company_sz(self):
        """归属公司选择深圳查询"""
        self.jggl.open_url()
        self.jggl.company_sz()
        assert(self.jggl.company_check(),'深圳乐有家')


    def test_company_zs(self):
        """归属公司选择中山查询"""
        self.jggl.open_url()
        self.jggl.company_zs()
        assert(self.jggl.company_check(),'中山乐有家')


    def test_areas(self):
        """省市区查询"""
        self.jggl.open_url()
        self.jggl.areas()
        assert(self.jggl.areas_check(),'南山区')


    def test_organization_type_jt(self):
        """机构类型选择集团查询"""
        self.jggl.open_url()
        self.jggl.organization_type_jt()
        assert(self.jggl.organization_type_check(),'集团')


    def test_organization_type_zgs(self):
        """机构类型选择子公司查询"""
        self.jggl.open_url()
        self.jggl.organization_type_zgs()
        assert(self.jggl.organization_type_check(),'子公司')


    def test_organization_type_fzjg(self):
        """机构类型选择分支机构查询"""
        self.jggl.open_url()
        self.jggl.organization_type_fzjg()
        assert(self.jggl.organization_type_check(),'分支机构')


    def test_organization_type_qt(self):
        """机构类型选择其他查询"""
        self.jggl.open_url()
        self.jggl.organization_type_qt()
        assert(self.jggl.organization_type_check(),'其他')


    def test_mechanism_status_zxz(self):
        """机构状态选择装修中查询"""
        self.jggl.open_url()
        self.jggl.mechanism_status_zxz()
        assert(self.jggl.mechanism_status_check(),'装修中')


    def test_mechanism_status_yyz(self):
        """机构状态选择营业中查询"""
        self.jggl.open_url()
        self.jggl.mechanism_status_yyz()
        assert(self.jggl.mechanism_status_check(),'营业中')


    def test_mechanism_status_ycp(self):
        """机构状态选择已撤铺查询"""
        self.jggl.open_url()
        self.jggl.mechanism_status_ycp()
        assert(self.jggl.mechanism_status_check(),'已撤铺')


    def test_keyword(self):
        """关键字查询"""
        self.jggl.open_url()
        self.jggl.keyword()
        assert(self.jggl.keyword_check(),'测试一分行')