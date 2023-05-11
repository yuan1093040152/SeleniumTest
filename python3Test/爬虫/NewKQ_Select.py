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
import traceback
from datetime import datetime



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

    def __init__(self,browser,url):
        self.browser = open_browser(browser, url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)


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
            'token': "29ca2596ea2a45b494e692118389c0b7",
            'aid': "APP002",
            'ssid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'v': "3",
            'imei': "fe8222e5f1a629e422347af7597af794014b86fb",
            'carries': "1",
            'latitude': "22.57049",
            'cache-control': "no-cache",
            'postman-token': "d01b2316-648b-92ee-c5b5-f81d22096981"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

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
            'clientsign': "0458e0eefc32c02bf36a8b1bb96fe2d1",
            'workerno': "252613",
            'appversion': "6.0.0.0",
            'token': "29ca2596ea2a45b494e692118389c0b7",
            'aid': "APP002",
            'ssid': "800150FB-E029-4F77-BD80-91715BE6FCDF",
            'v': "3",
            'imei': "fe8222e5f1a629e422347af7597af794014b86fb",
            'carries': "1",
            'latitude': "22.57049",
            'cache-control': "no-cache",
            'postman-token': "f422198d-70a9-166b-076a-b2881e370b51"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)


    def getcookie(self,empnumber,name,url2,xm):
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

        # for i in cookie:
        #     try:
        #         if '_smt_uid' == i['name']:
        #             _smt_uid_value = i['value']
        #             print('_smt_uid_value====', _smt_uid_value)
        #     except:
        #         pass

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

        # cookie = 'jjshome_uuid=%s; _smt_uid=%s; /hsl/index/house-list_guidance=1; /hsl/house/house-detail_guidance=1; /community/communityDic/communityDic-list_guidance=1; /community/communityDic/communityDic-detail_guidance=1; /community/communityDg/communityDg-list_guidance=1; /community/communityDg/communityDg-dic_guidance=1; /community/communityDic/communityDic-add-view-batch_guidance=1; /community/communityDg/communityDg-add-batch-cache_guidance=1; /hsl/entrust/entrust-add_guidance=1; /hsl/index/own-house-list_guidance=1; cookiesId=bce302d180064c60bd921167c696573c; _ga=GA1.2.317993357.1611364094; agentCardhd_time=1; fhListCookies=; gr_user_id=75926756-dfea-419b-a884-306d3cc99060; iJSESSIONID=57F9684687F6B8DDAEEAC86F8098123E; testLEYOUJIA=ZWNmZGIzOWYtYzhhNi00MTEzLTk2NzgtNGE0ODJmMjA1MjZl; SESSION=OWE3MTAzMjAtYjk2Ny00ZDEwLWFmZjAtMWM2NjFjOTExYTU0; login-mac=6C-0B-84-A4-72-DD; SESSION=M2Q4OGExMGItZjMwNC00YzBiLTlhNzEtOTVjZWJmY2UzYmE4; _gid=GA1.2.1006926862.1622013004; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1621326471,1622013004,1622013731; Hm_lvt_728857c2e6b321292b2eb422213d1609=1622013004,1622013731; Hm_lpvt_728857c2e6b321292b2eb422213d1609=1622014000; Hm_lpvt_1851e6f08c8180e1e7b5e33fb40c4b08=1622014000; jjshome_sid=%s; default_city_code=000002; JSESSIONID-FANG=FD6178335901E442DE30A3662D4D90EE; JSESSIONID=%s; proLEYOUJIA=YjI3ZTY0OTktOWY5OS00ZmVlLWJlYWUtMTZjMTk2ZGMwZWI4; login-workerid=06045224' % (
        # jjshome_uuid_value, _smt_uid_value, jjshome_sid_value, JSESSIONID_value)

        cookie ='jjshome_uuid=%s; _smt_uid=; cookiesId=116347ef6ac44e45a1c414bf7b790d1b; _ga=GA1.2.1941642435.1637634248; agentCardhd_time=1; token=t.LmX27IZZvGOqM1DRudGm; prefs={}; fhListCookies=; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1640866512; Hm_lvt_728857c2e6b321292b2eb422213d1609=1640866512; gr_user_id=b4d54e60-5a65-41ea-815a-9de61463cd28; proLEYOUJIA=%s; JSESSIONID=%s; login-mac=6C-0B-84-A4-72-DD; login-workerid=06045224; jjshome_sid=%s'% (jjshome_uuid_value,proLEYOUJIA_value, jjshome_sid_value, JSESSIONID_value)
        print('cookie2===', cookie)

        # 将中文转换格式为URL编码，方便接口调用
        aa = [name, xm]
        bb = []
        for i in aa:
            cc = urllib.parse.quote(i)
            bb.append(cc)

        print(bb)
        nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print(nowtime)

        body2 = "opWorkerId=%s&queryPurview=&pageNum=1&pageSize=100&deptName=%s&deptNumber=5501462&workerName=%s&workerId=%s&scopeType=5&userTypeStr=&timeType=1&startTime=%s&endTime=%s" % (
        empnumber, bb[0], bb[1],empnumber,nowtime, nowtime)
        print('body2=', body2)

        headers2 = {
            'Host': 'i.leyoujia.com'
            , 'Connection': 'keep-alive'
            , 'Content-Length': '236'
            , 'Pragma': 'no-cache'
            , 'Cache-Control': 'no-cache'
            , 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"'
            , 'Accept': 'application/json, text/javascript, */*; q=0.01'
            , 'X-Requested-With': 'XMLHttpRequest'
            , 'sec-ch-ua-mobile': '?0'
            ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
            , 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            , 'Origin': 'https://i.leyoujia.com'
            , 'Sec-Fetch-Site': 'same-origin'
            , 'Sec-Fetch-Mode': 'cors'
            , 'Sec-Fetch-Dest': 'empty'
            , 'Referer': 'https://i.leyoujia.com/attend/main/index'
            , 'Accept-Encoding': 'gzip, deflate, br'
            , 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,'
            , 'Cookie': cookie
        }

        response2 = requests.request('post', url2, data=body2, headers=headers2, verify=False)
        print('response2====',response2.text)
        print('----------------------------------------')
        lists = json.loads(response2.text)['data']['list']
        print(lists)

        WDK_name = []
        WDK_id = []
        hh = time.strftime('%H', time.localtime(time.time()))
        print(hh)
        if int(hh) < 12:
            # 上班
            for i in lists:
                if i['upAttendStatusStr'] == '旷工':
                    WDK_name.append(i['workerName'])
                    WDK_id.append(i['workerId'])

                else:
                    pass
            print('请通知小伙伴们打上班卡')
        else:

            # 下班
            for i in lists:
                if i['nextAttendStatusStr'] == '旷工':
                    WDK_name.append(i['workerName'])
                    WDK_id.append(i['workerId'])

                else:
                    pass
            print('请通知小伙伴们打下班卡')

        print('未打卡人员名单：', WDK_name)
        print('未打卡人员名单ID：', WDK_id)

        self.browser.close()
        self.browser.quit()
        return WDK_name


    # 发送邮件函数
    def Email(self,info,WDK_name):

        response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(response_time)
        title = info
        # (",".join(str(i) for i in WDK_name  去列表数据并用逗号分割)
        content = '跟新时间：' + response_time + '\n' + '通知：\n      ' + info + ':\n      ' + ",".join(
            str(i) for i in WDK_name)
        # content = response_time+u'    成交列表响应时间为%s秒，请通知开发及时处理'%WDK_name
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "1093040152@qq.com"  # 用户名
        mail_pass = "pugbzjhrfpfqfeca"  # QQ邮箱登录的授权码
        # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
        receivers = ['袁猛<1093040152@qq.com>']
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(content, 'plain', 'utf-8')  # 文本内容
        message['From'] = '袁猛<1093040152@qq.com>'  # mail_user # 发送者   （发送人同QQ备注，可不写）
        message['To'] = ','.join(receivers)  # 这里必须要把多个邮箱按照逗号拼接为字符串
        subject = title  # 主题
        message['Subject'] = subject

        try:
            c = smtplib.SMTP()
            c.connect(mail_host, 25)  # 25 为 SMTP 端口号
            c.login(mail_user, mail_pass)  # 登录
            c.sendmail(mail_user, receivers, message.as_string())  # 发送
            print("邮件发送成功！")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")

        # ##############################################
        # 从dubbo后台获取直连ip

    def dubboGetip(self, interface, huanjing, tanchuangbz):

        '''
        # 从dobbo中心获取服务的直连ip。
        :param interface: 服务名称
        :param huanjing: 调用环境
        :param tanchuangbz: 当获取不到ip时是否弹窗确认打开dubbo后台管理中心
        :return:
        '''
        # 弹窗确认结果，默认为False
        ry = False
        if u'正式' in huanjing or u'生产' in huanjing:
            huanjing = '172.16.3.233:8084'
        elif u'3.100' in huanjing or u'线下测试' in huanjing:
            huanjing = '172.16.4.114:9080'
        elif u'22.100' in huanjing or u'容器' in huanjing:
            huanjing = '172.16.22.100:9080'
        elif u'2.54' in huanjing or u'线上测试' in huanjing:
            huanjing = '192.168.3.70:9080'
        else:
            print(u'环境指定错误，默认使用3.100')
            huanjing = '172.16.4.114:9080'
        try:
            headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate",
                       "Connection": "keep-alive",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                       "Host": "172.16.3.233:8084",
                       "Cookie": "_ga=GA1.1.1890888338.1580476038; HISTORY=\"com.jjshome.im.service.dubbo.NimAccidService..../governance/services/com.jjshome.im.service.dubbo.NimAccidService/providers\\.\\.\\.\\.\\.\\.com.jjshome.im.service.dubbo.INimRoomService..../governance/services/com.jjshome.im.service.dubbo.INimRoomService/providers\"",
                       "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                       "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}
            url = 'http://%s/governance/services/%s/providers' % (huanjing, interface)
            url_t = 'http://%s/governance/services?keyword=%s' % (huanjing, interface)
            # 发送请求，查询dubbo后台，获取ip和端口
            try:
                r = requests.get(url=url, headers=headers, timeout=5)
                r = re.findall('\d+\.\d+\.\d+\.\d+\:\d+', r.text)
            except:
                if tanchuangbz:
                    print("请求失败")
            # 如果获取ip和端口成功
            if r:
                print(r)
                print(re.split(':', r[0]))
                # 如果是容器则特殊处理
                if u'22.100' in huanjing or u'容器' in huanjing:
                    return ('172.16.22.100', '2008')
                return re.split(':', r[0])

        except:
            print("获取不到IP和端口")


     #发送乐聊通知提醒
    def IMsendinfo(self,ids, text, info,group='im-serve-attend',url=''):

        idsstr = ''
        # 如果是字符串则转为list
        if type(ids) != type([]):
            ids = ids.replace(';', ',')
            ids = ids.replace(u'，', ',')
            ids = re.split(',', ids)
        if ids:
            for i in ids:
                idsstr = u'%s"%s",' % (idsstr, i)
            idsstr = idsstr[:-1]
            print('idsstr:',idsstr)
        else:
            return

        msg = text.replace('\r\n', '')
        msg = msg.replace('\n', '')
        interface = 'com.jjshome.im.service.dubbo.NimAccidService'
        method = 'sendCustomMsg'
        # host = '192.168.196.6'    不知道什么原因这个IP会变，故不能写死
        # port = '26889'

        param = u'{"fromAccid":"servenumber000011","group":"%s","toAccids":[%s],"body":"{\\"type\\":8,\\"data\\":{\\"title\\":\\"%s\\",\\"content\\":\\"%s\\",\\"source\\":\\"im-serve-attend\\",\\"sourceName\\":\\"%s的温馨提示\\",\\"sourceType\\":\\"im-serve-fwsq\\",\\"url\\":\\"%s\\",\\"isOuterOpen\\":true}}"}' % (
            group, idsstr, info, msg, info, url)

        host, port = self.dubboGetip(interface=interface, huanjing=u'生产', tanchuangbz=False)

        try:
            url = u'http://172.16.100.12:29998/netdubbo'
            #改成utf-8解决中文乱码 （������С�������Ǵ��ϰ࿨）
            data = {'host': host, 'port': port, 'method': method, 'interface': interface, 'param': param, 'code': 'utf-8',
                    'outputbz': False}
            print('data =', data)
            req = requests.post(url=url, data=data, timeout=5)
            print(req.text)
            print(u'调用远程服务成功。')
        except:
            print(u'乐聊通知处理出错！')


global wechat_lock
wechat_lock = Lock()

# 这里可以设置UIDS, 多个人可同时接收 [袁猛，蔡姻，罗柳,王凯.....]
UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m','UID_dxNzj6aupA6Q4QZrDkwmCcDLMX2e','UID_pyB3i43mzt2LctecgCBZWBz035GZ','UID_IJVLOOwS4AtmaaydQzjBPoQUeBw0','UID_pLfwZ9GbaZjOco5HPv8eboziCrqc','UID_2CJ9rS2njM1tZlA41ZaW7JYwmnvZ','UID_dQjL40mX3SfNUOLQHjoR5xqbCUab']
# UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m']

APP_TOKEN = 'AT_wW7eEobXR61htcs4zw6HIchK1yUaSx8L'
# AT_zueTbAm3qrDJy2BvWtYwJwqVgRjGZIhF

class wechat_thread(Thread):
    """
    采用线程方式，不阻塞
    """

    def __init__(self, uids: list, content: str, topic_ids: list = [], url: str = '', app_token=''):

        # text：消息标题，最长为256，必填。
        # desp：消息内容，最长64Kb，可空，支持MarkDown。

        super(wechat_thread, self).__init__(name="wechat_thread")
        self.request_url = "http://wxpusher.zjiecode.com/api/send/message"
        self.uids = uids
        self.content = content
        self.topic_ids = topic_ids
        self.url = url
        self.lock = wechat_lock
        self.app_token = app_token if len(app_token) > 0 else APP_TOKEN

    def run(self):
        if self.content is None or len(self.content) == 0:
            return
        params = {}
        params['appToken'] = self.app_token
        params['content'] = self.content
        params['contentType'] = 1
        params['topicIds'] = self.topic_ids
        params['uids'] = self.uids
        params['url'] = self.url

        # 发送请求
        try:
            response = requests.post(self.request_url, json=params).json()
            if not response.get('success', False):
                print(response)
        except Exception as e:
            print("{} wechat_thread sent failed! ex:{},trace:{}".format(datetime.now(), str(e), traceback.format_exc()),
                  file=sys.stderr)
            return

        print("未打卡人员微信通知成功!")


def send_wx_msg(*args, **kwargs):
    """
    发送微信Msg
    :param content:   发送内容
    :return:
    https://wxpusher.zjiecode.com/admin/main/wxuser/list
    应用管理--关注应用  用户扫描此二维码，WxPuhsher会回调UID给开发者，开发者可通过UID发送消息给用户。
    """
    content = kwargs.get('content', None)
    if content is None:
        if len(args) == 0:
            return
        content = args[0]
    if len(content) == 0:
        return


    if not isinstance(content, str):
        if isinstance(content, dict):
            content = '{}'.format(print(content))
        else:
            content = str(content)

    uids = kwargs.get('uids', [])
    # 没有配置的话，使用缺省UID
    if len(uids) == 0:
        uids.extend(UIDS)

    app_token = kwargs.get('app_token')

    t = wechat_thread(uids=UIDS, content=content, app_token=APP_TOKEN)
    t.daemon = False
    t.start()



if __name__ == '__main__':
    browser = 'Chrome'
    url = 'https://i.leyoujia.com/jjslogin/tologin'
    url2 = 'https://i.leyoujia.com/attend/main/doAttendList'
    username = '252613'
    password = 'mm711232'
    name = '测试部'
    xm = '袁猛'
    empnumber = '06045224'
    #乐聊通知名单
    ids = ["252613","412999","419544","405984","403963","089363","171342","436614","410622"]
    # ids = ["252613"]
    hh = time.strftime('%H', time.localtime(time.time()))
    print(hh)
    if int(hh) < 12:
        info = '请以下小伙伴别忘记打上班卡'
    else:
        info = '请以下小伙伴别忘记打下班卡'
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)


    p = Login(browser,url)
    p.login()
    WDK_name = p.getcookie(empnumber,name,url2,xm)

    # (",".join(str(i) for i in WDK_name  去列表数据并用逗号分割)
    text = '通知：' + response_time + '\n\n    ' + info + ':\n    ' + "\n    ".join(str(i) for i in WDK_name)


    if len(WDK_name) == 0:
        print('小伙伴都已打卡，不进行通知')
    else:
        # p.Email(info,WDK_name)
        send_wx_msg(text)
        p.IMsendinfo(ids, text, info,group='im-serve-attend',url='')

    print('-------------------end!-----------------------')




