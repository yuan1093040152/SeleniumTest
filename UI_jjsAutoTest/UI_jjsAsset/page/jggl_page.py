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
        #详情
        "zcxx": 'xpath=>//*[@id="jgRouter"]/a[2]',
        "czjl": 'xpath=>//*[@id="jgRouter"]/a[3]',
        "lszt": 'xpath=>//*[@id="jgRouter"]/a[4]',
        "jg_bj": 'xpath=>//*[@id="updateShopInfo"]',
        "bj_wylx": 'xpath=>//*[@id="updateJgShopForm"]/div[1]/div[8]/div/div/input',
        "bj_wylx_zl": 'xpath=>//*[@id="updateJgShopForm"]/div[1]/div[8]/div/div/ul/li[2]',
        "bj_yfwe": 'xpath=>//*[@id="updateJgShopForm"]/div[3]/div[6]/div/div/input',
        "bj_yfwe_no": 'xpath=>//*[@id="updateJgShopForm"]/div[3]/div[6]/div/div/ul/li[3]',
        "bj_bc": 'xpath=>//*[@id="updateShopInfoConfirm"]',
        "xgjgzt": 'xpath=>//*[@id="jgHeader"]/div/div/p[1]/span[2]/button[3]',
        "xg_zt": 'xpath=>//*[@id="importForm"]/div[2]/div[2]/select',
        "xg_yyz": 'xpath=>//*[@id="importForm"]/div[2]/div[2]/select/option[5]',
        "xg_bc": 'xpath=>//*[@id="importForm"]/div[3]/button[1]',
        "cktzxq": 'xpath=>//*[@id="cktzxq"]',
        "tz_htgl": 'xpath=>//*[@id="checkContract"]',
        "tz_sdfgl": 'xpath=>//*[@id="main-content"]/div/div[3]/div/div[3]/span[1]/a',
        "tz_zzgl": 'xpath=>//*[@id="license"]/a',

        # 校验字段
        "jy_cqlx": 'xpath=>//*[@id="contenBody"]/tr[1]/td[3]',
        "jy_gsgs": 'xpath=>//*[@id="contenBody"]/tr[1]/td[4]',
        "jy_cq": 'xpath=>//*[@id="contenBody"]/tr[1]/td[8]',
        "jy_jgmc": 'xpath=>//*[@id="contenBody"]/tr[1]/td[9]',
        "jy_jglx": 'xpath=>//*[@id="contenBody"]/tr[1]/td[10]',
        "jy_jgzt": 'xpath=>//*[@id="contenBody"]/tr[1]/td[13]',
        "jy_jgxq": 'xpath=>//*[@id="jgRouter"]/a[1]',
        "jy_zcxx": 'xpath=>//*[@id="jgRouter"]/a[2]',
        "jy_czjl": 'xpath=>//*[@id="jgRouter"]/a[3]',
        "jy_lszt": 'xpath=>//*[@id="jgRouter"]/a[4]',
        "jy_fhmc": 'xpath=>//*[@id="updateJgShopForm"]/div[1]/div[3]/span[2]',
        "jy_jgzt_yyz": 'xpath=>//*[@id="jgHeader"]/div/div/p[1]/span[1]',
        "jy_tzbgxq": 'xpath=>//*[@id="main-content"]/div/div/h2',
        "jy_htgl": 'xpath=>//*[@id="main-content"]/div/div/div[1]/a',
        "jy_sdfgl": 'xpath=>//*[@id="main-content"]/div/div/div[1]/a[1]',
        "jy_zzgl": 'xpath=>//*[@id="main-content"]/div[2]/div/div/a[1]',


    }

    # 跳转证照管理
    def jump_zzgl(self):
        self.d.click(self.element_data['tz_zzgl'])
        time.sleep(2)

    def jump_zzgl_check(self):
        self.d.get_text(self.element_data['jy_zzgl'])
        time.sleep(2)


    # 跳转水电费管理
    def jump_sdfgl(self):
        self.d.click(self.element_data['tz_sdfgl'])
        time.sleep(2)

    def jump_sdfgl_check(self):
        self.d.get_text(self.element_data['jy_sdfgl'])
        time.sleep(2)


    #跳转合同管理
    def jump_htgl(self):
        self.d.click(self.element_data['tz_htgl'])
        time.sleep(2)

    def jump_htgl_check(self):
        self.d.get_text(self.element_data['jy_htgl'])
        time.sleep(2)


    #跳转拓展报告
    def jump_tzbg(self):
        self.d.click(self.element_data['cktzxq'])
        time.sleep(2)

    def jump_tzbg_check(self):
        self.d.get_text(self.element_data['jy_tzbgxq'])
        time.sleep(2)


    #修改机构状态
    def edit_status(self):
        self.d.click(self.element_data['xgjgzt'])
        time.sleep(2)
        self.d.click(self.element_data['xg_zt'])
        time.sleep(2)
        self.d.click(self.element_data['xg_yyz'])
        time.sleep(2)
        self.d.click(self.element_data['xg_bc'])
        time.sleep(2)

    def edit_status_check(self):
        self.d.get_text(self.element_data['jy_jgzt_yyz'])
        time.sleep(2)


    #编辑机构
    def jg_edit(self):
        self.d.click(self.element_data['jg_bj'])
        time.sleep(2)
        self.d.click(self.element_data['bj_wylx'])
        time.sleep(2)
        self.d.click(self.element_data['bj_wylx_zl'])
        time.sleep(2)
        self.d.click(self.element_data['bj_yfwe'])
        time.sleep(2)
        self.d.click(self.element_data['bj_yfwe_no'])
        time.sleep(2)
        self.d.click(self.element_data['bj_bc'])
        time.sleep(2)

    def jg_edit_check(self):
        self.d.get_text(self.element_data['jy_fhmc'])
        time.sleep(2)


    #资产信息
    def asset_info(self):
        self.d.click(self.element_data['zcxx'])
        time.sleep(2)

    def asset_info_check(self):
        self.d.get_text(self.element_data['jy_zcxx'])
        time.sleep(2)


    #操作记录
    def record(self):
        self.d.click(self.element_data['czjl'])
        time.sleep(2)

    def record_check(self):
        self.d.get_text(self.element_data['jy_czjl'])


    # 历史状态
    def state(self):
        self.d.click(self.element_data['lszt'])
        time.sleep(2)

    def state_check(self):
        self.d.get_text(self.element_data['jy_lszt'])


     #机构管理
    def open_url(self):
        self.d.open(self.jgurl)
        time.sleep(2)

    # 机构详情
    def open_url_xq(self):
        self.d.open(self.jgxqurl)
        time.sleep(2)

    # 产权类型选择租赁查询
    def Property_type_zl(self):
        self.d.click(self.element_data['cqlx'])
        time.sleep(2)
        self.d.click(self.element_data['cqlx_zl'])
        time.sleep(2)
        self.d.click( self.element_data['cx'])
        time.sleep(2)

    # 产权类型选择自购物业查询
    def Property_type_zgwy(self):
        self.d.click(self.element_data['cqlx'])
        time.sleep(2)
        self.d.click(self.element_data['cqlx_zgwy'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])
        time.sleep(2)


    #产权类型校验
    def Property_type_check(self):
        self.d.get_text(self.element_data["jy_cqlx"])
        time.sleep(3)


    #归属公司选择深圳查询
    def company_sz(self):
        self.d.click(self.element_data['gsgs'])
        time.sleep(2)
        self.d.click(self.element_data['gsgs_sz'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])
        time.sleep(2)

    #归属公司选择中山查询
    def company_zs(self):
        self.d.click(self.element_data['gsgs'])
        time.sleep(2)
        self.d.click(self.element_data['gsgs_zs'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])
        time.sleep(2)

    #归属公司校验
    def company_check(self):
        self.d.get_text(self.element_data["jy_gsgs"])
        time.sleep(3)


    #省市区查询
    def areas(self):
        self.d.click(self.element_data['sf'])
        time.sleep(2)
        self.d.click(self.element_data['sf_gd'])
        time.sleep(2)
        self.d.click(self.element_data['cs'])
        time.sleep(2)
        self.d.click(self.element_data['cs_sz'])
        time.sleep(2)
        self.d.click(self.element_data['cq'])
        time.sleep(2)
        self.d.click(self.element_data['cq_ns'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])
        time.sleep(2)

    #省市区校验
    def areas_check(self):
        self.d.get_text(self.element_data["jy_cq"])
        time.sleep(3)


    #机构类型选择集团查询
    def organization_type_jt(self):
        self.d.click(self.element_data['jglx'])
        time.sleep(2)
        self.d.click(self.element_data['jglx_jt'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构类型选择子公司查询
    def organization_type_zgs(self):
        self.d.click(self.element_data['jglx'])
        time.sleep(2)
        self.d.click(self.element_data['jglx_zgs'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构类型选择分支机构查询
    def organization_type_fzjg(self):
        self.d.click(self.element_data['jglx'])
        time.sleep(2)
        self.d.click(self.element_data['jglx_fzjg'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构类型选择其它查询
    def organization_type_qt(self):
        self.d.click(self.element_data['jglx'])
        time.sleep(2)
        self.d.click(self.element_data['jglx_qt'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构类型校验
    def organization_type_check(self):
        self.d.get_text(self.element_data["jy_jglx"])
        time.sleep(3)


    # 机构状态选择装修中查询
    def mechanism_status_zxz(self):
        self.d.click(self.element_data['jgzt'])
        time.sleep(2)
        self.d.click(self.element_data['jgzt_zxz'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构状态选择营业中查询
    def mechanism_status_yyz(self):
        self.d.click(self.element_data['jgzt'])
        time.sleep(2)
        self.d.click(self.element_data['jgzt_yyz'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构状态选择已撤铺查询
    def mechanism_status_ycp(self):
        self.d.click(self.element_data['jgzt'])
        time.sleep(2)
        self.d.click(self.element_data['jgzt_ycp'])
        time.sleep(2)
        self.d.click(self.element_data['cx'])

    # 机构状态校验
    def mechanism_status_check(self):
        self.d.get_text(self.element_data["jy_jgzt"])
        time.sleep(3)


    # 关键字查询
    def keyword(self):
        self.d.send_key(self.element_data['jgzt'],'测试一分行')
        time.sleep(2)
        self.d.click(self.element_data['cx'])


    # 关键字查询校验
    def keyword_check(self):
        self.d.get_text(self.element_data["jy_jgmc"])
        time.sleep(3)

    #详情页校验
    def detail_page_check(self):
        self.d.get_text(self.element_data["jy_jgxq"])
        time.sleep(3)



    # # 关闭网页
    # def close_page(self):
    #     self.d.close()



class jggl(jgglList):
    pass