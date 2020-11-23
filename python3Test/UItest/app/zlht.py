#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/23 15:07
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

nox_adb.exe connect 127.0.0.1:62001

adb devices

查看哪个程序占用了adb端口  netstat -aon|findstr "5037"

通过PID找出进程   tasklist|findstr "10593"

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

    driver.find_element_by_name('始终允许').click()
    time.sleep(1)
    print('111111')

    driver.find_element_by_name('始终允许').click()
    time.sleep(1)
    print('222222222')

    driver.find_element_by_name('始终允许').click()
    time.sleep(1)

    driver.find_element_by_name('始终允许').click()
    time.sleep(1)

    driver.find_element_by_name("输入你的编号").send_keys('252613')

    driver.find_element_by_name("输入密码").send_keys('123456')

    driver.find_element_by_name("登 录").click()
    time.sleep(3)

    driver.find_element_by_name('始终允许').click()
    time.sleep(1)

    driver.find_element_by_name('我的').click()
    time.sleep(1)

    driver.find_element_by_name('电子合同').click()
    time.sleep(1)

    driver.find_element_by_name('新增合同').click()
    time.sleep(1)

    driver.find_element_by_name('租赁合同').click()
    time.sleep(1)

    driver.find_element_by_name('我知道了').click()
    time.sleep(1)

    driver.quit()
except Exception as e:

    driver.quit()
    print('結束')
    print(e)






