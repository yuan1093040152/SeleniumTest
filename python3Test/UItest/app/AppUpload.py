#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/1/7 15:20
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from appium import webdriver

import os,time


desired_caps = {}
#启动信息,启动appium后就可以找到下面参数信息
desired_caps['platformName'] = 'Android'    #设备系统
desired_caps['platformVersion'] = '10'      #设备系统版本
desired_caps['deviceName'] = 'HUAWEI P20'     #设备名称

desired_caps['appPackage'] = 'com.jjshome.oa'    #包名
desired_caps['appActivity'] = 'com.jjshome.oa.activity.StartActivity'   #启动名

#声明手机驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# "//*[@id='kw']"
time.sleep(3)

try:

    # driver.find_element_by_name('始终允许').click()
    # time.sleep(1)
    # print('111111')
    #
    # driver.find_element_by_name('始终允许').click()
    # time.sleep(1)
    # print('222222222')
    #
    # driver.find_element_by_name('始终允许').click()
    # time.sleep(1)
    #
    # driver.find_element_by_name('始终允许').click()
    # time.sleep(1)
    #
    # driver.find_element_by_name("输入你的编号").send_keys('252613')
    #
    # driver.find_element_by_name("输入密码").send_keys('mm711232')
    #
    # driver.find_element_by_name("登 录").click()
    # time.sleep(5)
    #
    # driver.find_element_by_name('始终允许').click()
    # time.sleep(3)
    #
    # driver.find_element_by_name('我的').click()
    # time.sleep(3)

    cmd1 = r"adb shell /system/bin/screencap -p /sdcard/3.png"  # 命令1：在手机上截图3.png为图片名
    cmd2 = r"adb pull /sdcard/3.png E:\test\3.png"  # 拉取手机图片文件保存到电脑上
    os.system(cmd1)
    time.sleep(3)
    os.system(cmd2)

    driver.quit()

except Exception as e:
    driver.quit()
    print('結束')
    print(e)