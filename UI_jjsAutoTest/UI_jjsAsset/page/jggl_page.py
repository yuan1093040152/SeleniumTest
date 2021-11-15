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
from UI_jjsAutoTest.UI_jjsAsset.lib import read_config
import time

#机构管理
class jgglList(LoginPage):

    element_data = {
        #产权类型
        "cqlx":'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/input',
        "cqlx_zl": 'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/ul/li[2]',
        "cqlx_zgwy": 'xpath=>//*[@id="myForm"]/div/div[1]/div[1]/div/ul/li[3]',
        #归属公司
        "gsgs": 'xpath=>//*[@id="myForm"]/div/div[1]/div[2]/div/input',
        "gsgs_sz": 'xpath=>//*[@id="myForm"]/div/div[1]/div[2]/div/ul/li[3]',
        "gsgs_zs": 'xpath=>//*[@id="myForm"]/div/div[1]/div[2]/div/ul/li[7]',
        # 省市区
        "sf": 'xpath=>//*[@id="myForm"]/div/div[1]/div[3]/div/input',
        "sf_gd": 'xpath=>//*[@id="myForm"]/div/div[1]/div[3]/div/ul/li[10]',
        "cs": 'xpath=>//*[@id="myForm"]/div/div[1]/div[4]/div/input',
        "cs_sz": 'xpath=>//*[@id="myForm"]/div/div[1]/div[4]/div/ul/li[2]',
        "cq": 'xpath=>//*[@id="myForm"]/div/div[1]/div[5]/div/input',
        "cq_ns": 'xpath=>//*[@id="myForm"]/div/div[1]/div[5]/div/ul/li[3]',
        # 机构类型
        "jglx": 'xpath=>//*[@id="myForm"]/div/div[1]/div[6]/div/input',
        "jglx_jt": 'xpath=>//*[@id="myForm"]/div/div[1]/div[6]/div/ul/li[2]',
        "jglx_zgs": 'xpath=>//*[@id="myForm"]/div/div[1]/div[6]/div/ul/li[3]',
        "jglx_fzjg": 'xpath=>//*[@id="myForm"]/div/div[1]/div[6]/div/ul/li[4]',
        "jglx_qt": 'xpath=>//*[@id="myForm"]/div/div[1]/div[6]/div/ul/li[5]',
        # 机构状态
        "jgzt": 'xpath=>//*[@id="myForm"]/div/div[1]/div[7]/div/input',
        "jgzt_zxz": 'xpath=>//*[@id="myForm"]/div/div[1]/div[7]/div/ul/li[4]',
        "jgzt_yyz": 'xpath=>//*[@id="myForm"]/div/div[1]/div[7]/div/ul/li[5]',
        "jgzt_ycp": 'xpath=>//*[@id="myForm"]/div/div[1]/div[7]/div/ul/li[9]',
        # 关键字
        "gjz": 'xpath=>//*[@id="myForm"]/div/div[1]/div[13]/input',
        # 查询
        "cx": 'xpath=>//*[@id="chaxun"]',
        # 校验字段
        "jy_cqlx": 'xpath=>//*[@id="contenBody"]/tr[1]/td[3]',
        "jy_gsgs": 'xpath=>//*[@id="contenBody"]/tr[1]/td[4]',
        "jy_cq": 'xpath=>//*[@id="contenBody"]/tr[1]/td[8]',
        "jy_jgmc": 'xpath=>//*[@id="contenBody"]/tr[1]/td[9]',
        "jy_jglx": 'xpath=>//*[@id="contenBody"]/tr[1]/td[10]',
        "jy_jgzt": 'xpath=>//*[@id="contenBody"]/tr[1]/td[13]',


    }


    def open_url(self):
        # self.d.open("https://coatest.leyoujia.com/jg/manage/toManageList")
        self.d.open(self.jgurl)
        time.sleep(2)

    # 产权类型选择租赁查询
    def Property_type(self):
        self.d.click(self.element_data['cqlx'])
        time.sleep(2)
        self.d.click(self.element_data['cqlx_zl'])
        time.sleep(2)
        self.d.click( self.element_data['cx'])
        time.sleep(2)


    # # 关闭网页
    # def close_page(self):
    #     self.d.close()


    #校验
    def check(self):
        self.d.get_text(self.element_data["accountList01"])
        time.sleep(3)




class jggl(jgglList):
    pass