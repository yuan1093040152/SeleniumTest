#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/12 13:57
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from UI_jjsAutoTest.UI_jjsAsset.page.login_page import LoginPage
import time

#机构管理
class jgglList(LoginPage):

    element_data = {
        "cqlx":'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/input',
        "cqlx_zl": 'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/ul/li[2]',
        "cqlx_zgwy": 'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/ul/li[3]',
        "cx": 'xpath=>//*[@id="chaxun"]',
        "": "",
        "": "",
        "": "",


    }

    def open_url(self):
        self.d.open("https://coatest.leyoujia.com/jg/manage/toManageList")
        time.sleep(2)

    # 产权类型选择租赁查询
    def Property_type(self):
        self.d.click(self.element_data['cqlx'])
        time.sleep(2)
        self.d.click(self.element_data['cqlx_zl'])
        time.sleep(2)
        self.d.click( self.element_data['cx'])
        time.sleep(2)

    def close_page(self):
        # 关闭网页
        self.d.close()



class jggl(jgglList):
    pass