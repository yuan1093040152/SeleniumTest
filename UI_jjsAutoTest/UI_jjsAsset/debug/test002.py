#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/10 9:35
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from UI_jjsAutoTest.UI_jjsAsset.lib.pc_login import login
from UI_jjsAutoTest.UI_jjsAsset.lib.openbrowser import testname
from UI_jjsAutoTest.UI_jjsAsset.page.jggl_list_XX import jgglList
from selenium.webdriver.common.by import By
from selenium import webdriver


def aa ():

    login().itestlogin()


    # testname.ClickElement(By.XPATH,"//li[14]/ul[@class='second-menu']/li[11]/a[@class='menuLevel_2']")
    js = 'window.open("https://coatest.leyoujia.com/jg/manage/toManageList")'
    # testname.execute(js)

    # # jgglList.open_url(js)

    login().Time(5)


if __name__ == '__main__':
    aa()