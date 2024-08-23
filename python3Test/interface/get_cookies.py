#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/5/11 10:50
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
"""
1.UI打开新系统页面 并获取所有COOKIES
2.https://i.leyoujia.com/jjslogin/getRCodeToken   获取这个接口的返回
3.https://i.leyoujia.com/jjslogin/scanCheck  扫码，把1当请求头,2当参数
4.https://i.leyoujia.com/jjslogin/scanLogin  登录  把1当请求头,2当参数

"""
import re
import urllib.request,cv2

from PIL import Image
from pyzbar.pyzbar import decode

from selenium.webdriver.common.by import By
from selenium import webdriver
from email.mime.text import MIMEText
import json,time,smtplib
import urllib.parse
from threading import Lock, Thread
import requests
import sys
import traceback,argparse
from datetime import datetime
from email.header import Header



 #判断运行浏览器
def open_browser(browser,url):
    if browser == 'Chrome':
        #添加忽略ssl证书，接收不信任的认证
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        return driver

    elif browser == 'Firefox':
        # 添加忽略ssl证书，接收不信任的认证
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.get(url)
        return driver

    else:
        pass


class Login():

    def jenkins(self):
        # 获取jenkins传递过来的参数
        parser = argparse.ArgumentParser()
        parser.add_argument("token")
        args = parser.parse_args()
        param = vars(args)
        token = param['token']
        print('token======',token)
        return token


    def __init__(self,browser,url):

        self.browser = open_browser(browser, url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.token = self.jenkins()
        #调试用
        # self.token = '7dee6881ed5a8ab4b9d51c720606b410'


    # 输入
    def ImputElement(self, type, element, value):
        self.browser.find_element(by=type, value=element).send_keys(value)

    # 清除
    def CleanElement(self, type, element):
        self.browser.find_element(by=type, value=element).clear()

    # 点击
    def ClickElement(self, type, element):
        self.browser.find_element(by=type, value=element).click()

    # 关闭窗口
    def Close(self):
        self.browser.close()

    # 关闭浏览器
    def Quit(self):
        self.browser.quit()

    # 时间
    def Time(self, s):
        time.sleep(s)

    # 等待
    def Wait(self, s):
        self.browser.implicitly_wait(s)

        # 通过元素获取验证码
    def getcode(self):
        # 方法一：通过元素获取验证码
        path = '123.png'
        path1 = '1234.png'
        # 截图整个页面
        self.browser.save_screenshot(path)
        # 获取元素的坐标（x为上，y为左，w为下，h为右，减为上移，加为下移）
        img1 = self.browser.find_element(By.ID, 'code')
        left = img1.location['x'] - 10
        top = img1.location['y'] - 10
        Width = left + img1.size['width'] + 10
        Height = top + img1.size['height'] + 10
        print(left, top, Width, Height)
        picture = Image.open(path)
        # 根据上面的元素坐标裁剪图片
        picture = picture.crop((left, top, Width, Height))
        picture.save(path1)

        # 读取图像文件
        img = cv2.imread(path1)

        # 解码二维码
        decoded_qr_codes = decode(img)
        print(decoded_qr_codes)

        # 输出解码结果
        for code in decoded_qr_codes:
            rCodeToken = code.data.decode('utf-8')[-4:]
            print(rCodeToken)
            return rCodeToken


    #登录
    def login(self):
        self.Time(5)
        # 通过js新开一个窗口
        js = 'window.open("https://localhost.leyoujia.com:25982/CLodopfuncs.js")'
        self.browser.execute_script(js)
        self.Time(3)
        rCodeToken = self.getcode()
        print('rCodeToken====',rCodeToken)

        cookie = self.browser.get_cookies()
        print('cookie===', cookie)
        for i in cookie:
            try:
                if 'jjshome_sid' == i['name']:
                    jjshome_sid_value = i['value']
                    print('jjshome_sid_value====', jjshome_sid_value)
            except:
                pass

        for i in cookie:
            try:
                if 'jjshome_uuid' == i['name']:
                    jjshome_uuid_value = i['value']
                    print('jjshome_uuid_value====', jjshome_uuid_value)
            except:
                pass


        for i in cookie:
            try:
                if 'JSESSIONID' == i['name']:
                    JSESSIONID_value = i['value']
                    print('JSESSIONID_value====', JSESSIONID_value)
            except:
                pass

        for i in cookie:
            try:
                if 'proLEYOUJIA' == i['name']:
                    proLEYOUJIA_value = i['value']
                    print('proLEYOUJIA_value====', proLEYOUJIA_value)
            except:
                pass

        print('------------------------------')

        cookie1 ='lyj_login_w_no=029246; jjshome_uuid=%s; _smt_uid=625fb187.4c1d6965; prefs={}; cookiesId=7d8ef6ac0d454f9a8c027e214cbe682f; agentCardhd_time=1; fhListCookies=; gr_user_id=519db3c6-8d95-44d0-abe8-0ee036500e5d; /hsl/index/house-list_guidance=1; lyj_analysis_pageCookie=1176%%3A2; applyTaskGuide=02081317; csrftoken=5PjyIGdNVAIJVC6LlkA1eFzLfYY3uH62b9ARkVejXuErWID13ivGqZY9OmhdSVb7; /hsl/house/house-detail_guidance=1; /hsl/entrust/entrust-add_guidance=1; connect.sid=s%%3AYzeTEgj5S8WQy23I5OR67P0AwxkCdjiw.cBZ65edt94fce1R4ns4VqaShnGKg6c2q2VwjgQrxS%%2Fk; token=t.ZolH0dnGX4IhzKqZbItX; default_city_code=000002; JSESSIONID-FANG=YzhmY2Q2ZjEtMzliZS00ZmIwLTlmNjgtZTE0ZTJhMDNjNTI3; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1682302655,1683620667; Hm_lpvt_1851e6f08c8180e1e7b5e33fb40c4b08=1683620667; Hm_lvt_728857c2e6b321292b2eb422213d1609=1682302655,1683620667; Hm_lpvt_728857c2e6b321292b2eb422213d1609=1683620667; login-workerid=06045224; login-mac=CB8222B5C1a629B422347aC7597aC794014b86Cb; jjshome_sid=%s; JSESSIONID=%s; proLEYOUJIA=%s'% (jjshome_uuid_value, jjshome_sid_value, JSESSIONID_value,proLEYOUJIA_value)
        print('cookie1===', cookie1)

        # 若登录失败更换token
        url = "https://i.leyoujia.com/jjslogin/scanCheck"
        self.Time(2)
        payload = "rCodeToken=%s"%rCodeToken
        print(payload)
        headers = {
            'host': "i.leyoujia.com",
            'deptnumber': "5501462",
            'timestamp': "1683769915",
            'mobilemodel': "iPhone",
            'appname': "ios-jjr",
            'deviceid': "B002EFA1-665A-3A53-8E9D-B22204CE026C",
            'd': "0",
            'methodcode': "70001",
            'accept': "*/*",
            'app_name': "JJSOA",
            'phoneos': "ios",
            'bundle_identifier': "com.jjshome.oa",
            'content-length': "15",
            'accept-encoding': "gzip, deflate, br",
            'user-agent': "JJSOffice/6.0.0.0 (iPhone; iOS 16.1; Scale/2.00)",
            'cookie':cookie1,
            'x-requested-with': "XMLHttpRequest",
            'phonemodel': "iPhone 11",
            'uuid': "B002EFA1-665A-3A53-8E9D-B22204CE026C",
            'version': "6.0.0.0",
            'network': "4G",
            'clientid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'channel': "APP Store",
            'mobileno': "Ag5LQmtUrMWtd8qvRcYV2A==",
            'source': "from_self",
            'empnumber': "06045224",
            'empno': "06045224",
            'opid': "06045224",
            'longitude': "114.1057",
            'accept-language': "zh-Hans-CN;q=1",
            'idfa': "00000000-0000-0000-0000-000000000000",
            'mobile': "Ag5LQmtUrMWtd8qvRcYV2A==",
            'cit': "000002",
            'authorization': "OGFHdVRLWlRTMThGUDBvQjNSQ0h2UT09",
            'connection': "keep-alive",
            'content-type': "application/x-www-form-urlencoded",
            'servicecode': "40001",
            'clientsign': "8c2879a5abdf9ec3ab62c2daee5d9a97",
            'workerno': "252613",
            'appversion': "6.0.0.0",
            'token': self.token,
            'aid': "APP002",
            'ssid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'v': "3",
            'imei': "fe8222e5f1a629e422347af7597af794014b86fb",
            'carries': "1",
            'latitude': "22.57049",
            'cache-control': "no-cache",
            'postman-token': "d01b2316-648b-92ee-c5b5-f81d22096981"
        }

        response = requests.request("POST", url, data=payload, headers=headers,verify=False)
        print(response.text)

        #若登录失败更换token
        url = "https://i.leyoujia.com/jjslogin/scanLogin"
        self.Time(2)
        payload = "rCodeToken=%s"%rCodeToken
        headers = {
            'host': "i.leyoujia.com",
            'deptnumber': "5501462",
            'timestamp': "1683772273",
            'mobilemodel': "iPhone",
            'appname': "ios-jjr",
            'deviceid': "B002EFA1-665A-3A53-8E9D-B22204CE026C",
            'd': "0",
            'methodcode': "70001",
            'accept': "*/*",
            'app_name': "JJSOA",
            'phoneos': "ios",
            'bundle_identifier': "com.jjshome.oa",
            'content-length': "15",
            'accept-encoding': "gzip, deflate, br",
            'user-agent': "JJSOffice/6.0.0.0 (iPhone; iOS 16.1; Scale/2.00)",
            'cookie': cookie1,
            'x-requested-with': "XMLHttpRequest",
            'phonemodel': "iPhone 11",
            'uuid': "B002EFA1-665A-3A53-8E9D-B22204CE026C",
            'version': "6.0.0.0",
            'network': "4G",
            'clientid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'channel': "APP Store",
            'mobileno': "Ag5LQmtUrMWtd8qvRcYV2A==",
            'source': "from_self",
            'empnumber': "06045224",
            'empno': "06045224",
            'opid': "06045224",
            'longitude': "114.1057",
            'accept-language': "zh-Hans-CN;q=1",
            'idfa': "00000000-0000-0000-0000-000000000000",
            'mobile': "Ag5LQmtUrMWtd8qvRcYV2A==",
            'cit': "000002",
            'authorization': "OGFHdVRLWlRTMThGUDBvQjNSQ0h2UT09",
            'connection': "keep-alive",
            'content-type': "application/x-www-form-urlencoded",
            'servicecode': "40001",
            'clientsign': "0c073a8c8a3e4a02ff7556478e203d3d",
            'workerno': "252613",
            'appversion': "6.0.0.0",
            'token': self.token,
            'aid': "APP002",
            'ssid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'v': "3",
            'imei': "fe8222e5f1a629e422347af7597af794014b86fb",
            'carries': "1",
            'latitude': "22.57049",
            'cache-control': "no-cache",
            'postman-token': "f422198d-70a9-166b-076a-b2881e370b51"
        }

        response = requests.request("POST", url, data=payload, headers=headers,verify=False)

        print(response.text)


    def getcookie(self):
        #通过js新开一个窗口
        js = 'window.open("https://i.leyoujia.com/attend/main/index")'
        self.browser.execute_script(js)
        time.sleep(2)
        cookie = self.browser.get_cookies()
        print('cookie1===',cookie)

        for i in cookie:
            try:
                if 'jjshome_sid' == i['name']:
                    jjshome_sid_value = i['value']
                    print('jjshome_sid_value====', jjshome_sid_value)
            except:
                pass

        for i in cookie:
            try:
                if 'jjshome_uuid' == i['name']:
                    jjshome_uuid_value = i['value']
                    print('jjshome_uuid_value====', jjshome_uuid_value)
            except:
                pass


        for i in cookie:
            try:
                if 'JSESSIONID' == i['name']:
                    JSESSIONID_value = i['value']
                    print('JSESSIONID_value====', JSESSIONID_value)
            except:
                pass

        for i in cookie:
            try:
                if 'proLEYOUJIA' == i['name']:
                    proLEYOUJIA_value = i['value']
                    print('proLEYOUJIA_value====', proLEYOUJIA_value)
            except:
                pass

        print('------------------------------')


        cookie ='jjshome_uuid=%s; _smt_uid=; cookiesId=116347ef6ac44e45a1c414bf7b790d1b; _ga=GA1.2.1941642435.1637634248; agentCardhd_time=1; token=t.LmX27IZZvGOqM1DRudGm; prefs={}; fhListCookies=; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1640866512; Hm_lvt_728857c2e6b321292b2eb422213d1609=1640866512; gr_user_id=b4d54e60-5a65-41ea-815a-9de61463cd28; proLEYOUJIA=%s; JSESSIONID=%s; login-mac=6C-0B-84-A4-72-DD; login-workerid=06045224; jjshome_sid=%s'% (jjshome_uuid_value,proLEYOUJIA_value, jjshome_sid_value, JSESSIONID_value)
        print('cookie===', cookie)

        print('cookie:',cookie)
        x = {'cookie':cookie}

        self.browser.close()
        self.browser.quit()
        return x


def getcookies():
    browser = 'Chrome'
    url = 'https://i.leyoujia.com/jjslogin/tologin'
    url2 = 'https://i.leyoujia.com/attend/main/doAttendList'
    username = '252613'
    password = 'mm252613'
    name = '测试部'
    xm = '袁猛'
    empnumber = '06045224'

    p = Login(browser, url)
    p.login()
    x = p.getcookie()

getcookies()