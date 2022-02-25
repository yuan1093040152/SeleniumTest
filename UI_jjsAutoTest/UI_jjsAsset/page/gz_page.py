#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/2/25 15:31
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from UI_jjsAutoTest.UI_jjsAsset.page.login_page import LoginPage
import time

#机构管理
class gzList(LoginPage):

    element_data ={
        # 固定版本盖章
        "title_1": 'xpath=>//*[@id="applyTitle"]',
        "remarks_1": 'xpath=>//*[@id="remark"]',
        "gzlb_1": 'xpath=>//*[@id="seal"]/div[2]/div[2]/label/input',
        "gzlb_1_input": 'xpath=>//*[@id="seal"]/div[2]/div[2]/div/div/input',
        "gzlb_1_input_1": 'xpath=>/html/body/ul[@id="ui-id-4"]/li[@class="ui-menu-item"][1]',
        "khzm_1": 'xpath=>//*[@id="fixed"]/div[2]/span[6]/label/input',
        "khzm_1_input": 'xpath=>//*[@id="fixed"]/div[2]/span[6]/input',
        "sfxykd_1": 'xpath=>//*[@id="needExpressDiv"]/div[2]/label[2]/input',
        "submit_1": 'xpath=>//*[@id="commit"]',
        "determine_1": 'xpath=>//*[@id="confire"]',
        "jy_title_1": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 店铺告知函盖章申请
        "jy_title_2": 'xpath=>//*[@id="main-content"]/div/div/h2',

        # 收入证明盖章
        "jy_title_3": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 实习/在职/小区证明/荣誉证书盖章
        "jy_title_4": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 借章外出申请
        "jy_title_5": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 项目结佣表/结算表盖章
        "jy_title_6": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 催告函盖章
        "jy_title_7": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 其他盖章
        "jy_title_8": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 租赁备案合同盖章申请
        "jy_title_9": 'xpath=>//*[@id="main-content"]/div/div[1]/h2',

        # 无法备案盖章申请
        "jy_title_10": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',

        # 采购合同盖章申请
        "jy_title_11": 'xpath=>//*[@id="main-content"]/div[1]/div/h2',



    }



    # 乐有家控股集团林凤辉申请盖章 - 固定版本盖章
    def open_gz_gdbb_url(self):
        self.d.open(self.gz_gdbb_url)
        time.sleep(2)

    def gz_gdbb_url_check(self):
        self.d.get_text(self.element_data["jy_title_1"])
        time.sleep(3)



    # 店铺租赁合同/解除协议/店铺告知函盖章申请
    def open_gz_dpgzh_url(self):
        self.d.open(self.gz_dpgzh_url)
        time.sleep(2)

    def gz_dpgzh_url_check(self):
        self.d.get_text(self.element_data["jy_title_2"])



    # 乐有家控股集团林凤辉申请盖章 - 收入证明盖章
    def open_gz_srzm_url(self):
        self.d.open(self.gz_srzm_url)
        time.sleep(2)

    def gz_srzm_url_check(self):
        self.d.get_text(self.element_data["jy_title_3"])



    # 乐有家控股集团林凤辉申请盖章 - 实习/在职/小区证明/荣誉证书盖章
    def open_gz_ryzs_url(self):
        self.d.open(self.gz_ryzs_url)
        time.sleep(2)

    def gz_ryzs_url_check(self):
        self.d.get_text(self.element_data["jy_title_4"])



    # 乐有家控股集团林凤辉申请盖章 - 借章外出申请
    def open_gz_jzwc_url(self):
        self.d.open(self.gz_jzwc_url)

    def gz_jzwc_url_check(self):
        self.d.get_text(self.element_data["jy_title_5"])



    # 乐有家控股集团林凤辉申请盖章 - 项目结佣表/结算表盖章
    def open_gz_xmjyb_url(self):
        self.d.open(self.gz_xmjyb_url)

    def gz_xmjyb_url_check(self):
        self.d.get_text(self.element_data["jy_title_6"])



    # 乐有家控股集团林凤辉申请盖章 - 催告函盖章
    def open_gz_cgh_url(self):
        self.d.open(self.gz_cgh_url)

    def gz_cgh_url_check(self):
        self.d.get_text(self.element_data["jy_title_7"])



    # 乐有家控股集团林凤辉申请盖章 - 其他盖章
    def open_gz_qt_url(self):
        self.d.open(self.gz_qt_url)

    def gz_qt_url_check(self):
        self.d.get_text(self.element_data["jy_title_8"])



    # 乐有家控股集团林凤辉申请盖章 - 租赁备案合同
    def open_gz_zlbaht_url(self):
        self.d.open(self.gz_zlbaht_url)

    def gz_zlbaht_url_check(self):
        self.d.get_text(self.element_data["jy_title_9"])



    # 乐有家控股集团林凤辉申请盖章 - 无法备案
    def open_gz_wfba_url(self):
        self.d.open(self.gz_wfba_url)

    def gz_wfba_url_check(self):
        self.d.get_text(self.element_data["jy_title_10"])



    # 乐有家控股集团林凤辉申请盖章-采购合同
    def open_gz_cght_url(self):
        self.d.open(self.gz_cght_url)

    def gz_cght_url_check(self):
        self.d.get_text(self.element_data["jy_title_11"])




    # 关闭网页
    def close_page(self):
        self.d.close()

    # 退出网页
    def quit_page(self):
        self.d.quit()



class gzgl(gzList):
    pass