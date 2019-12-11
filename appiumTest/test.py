#coding=utf-8
from appium import webdriver
from PIL import Image
from aip import AipOcr
from AppiumLibrary import *
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

desired_caps = {}
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] = '12.0'
desired_caps['deviceName'] = 'iPhone XR'
desired_caps['bundleId'] = 'com.jjshome.exam.test'
# desired_caps['udid'] = '4d377e0e3f8eac5bccb8c3cbc249c0aa8088bfc7'
# desired_caps['appActivity'] = 'com.jjshome.optionalexam.ui.main.WelcomeActivity'  # 乐学堂的activity
driver = webdriver.Remote('http://172.16.9.250:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]')