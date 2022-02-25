#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 16:11
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
from UI_jjsAutoTest.UI_jjsAsset.lib import pc_login
from UI_jjsAutoTest.UI_jjsAsset.lib import openbrowser
from selenium.webdriver.common.by import By


#机构管理
class jgglList(pc_login.login):

    element_data = {
        "cqlx_zl": "//div[@class='combo-select combo-open']/ul[@class='combo-dropdown']/li[@class='option-item'][1]",
        "cqlx_zgwy": "//div[@class='combo-select combo-open']/ul[@class='combo-dropdown']/li[@class='option-item'][2]",
        "cx": "//button[@id='chaxun']",
        "": "",
        "": "",
        "": "",


    }



    #打开机构管理
    def open_url(self):
        # pass

        js = 'window.open("https://coatest.leyoujia.com/jg/manage/toManageList")'
        self.execute(js)



    #产权类型选择租赁查询
    def Property_type(self):
        self.ClickElement(By.XPATH,self.element_data['cqlx_zl'])
        self.Time(2)
        self.ClickElement(By.XPATH,self.element_data['cx'])
        self.Time(3)



