# coding=utf-8

from email.mime.text import MIMEText
import requests, json, time, smtplib, re, MySQLdb, hashlib, sys, os
import re
import urllib.request, cv2

from PIL import Image
from pyzbar.pyzbar import decode

from selenium.webdriver.common.by import By
from selenium import webdriver
from email.mime.text import MIMEText
import json, time, smtplib
import urllib.parse
from threading import Lock, Thread
import requests
import sys
import traceback, argparse
from datetime import datetime
from email.header import Header


# 判断运行浏览器
def open_browser(browser, url):
    if browser == 'Chrome':
        # 添加忽略ssl证书，接收不信任的认证
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
        # parser = argparse.ArgumentParser()
        # parser.add_argument("token")
        # args = parser.parse_args()
        # param = vars(args)
        # token = param['token']
        token = os.environ['token']
        print('token======', token)
        return token

    def __init__(self, browser, url):

        self.browser = open_browser(browser, url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.token = self.jenkins()

    # 调试用
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

    # 登录
    def login(self):
        self.Time(5)
        # 通过js新开一个窗口
        js = 'window.open("https://localhost.leyoujia.com:25982/CLodopfuncs.js")'
        self.browser.execute_script(js)
        self.Time(3)
        rCodeToken = self.getcode()
        print('rCodeToken====', rCodeToken)

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

        cookie1 = 'lyj_login_w_no=029246; jjshome_uuid=%s; _smt_uid=625fb187.4c1d6965; prefs={}; cookiesId=7d8ef6ac0d454f9a8c027e214cbe682f; agentCardhd_time=1; fhListCookies=; gr_user_id=519db3c6-8d95-44d0-abe8-0ee036500e5d; /hsl/index/house-list_guidance=1; lyj_analysis_pageCookie=1176%%3A2; applyTaskGuide=02081317; csrftoken=5PjyIGdNVAIJVC6LlkA1eFzLfYY3uH62b9ARkVejXuErWID13ivGqZY9OmhdSVb7; /hsl/house/house-detail_guidance=1; /hsl/entrust/entrust-add_guidance=1; connect.sid=s%%3AYzeTEgj5S8WQy23I5OR67P0AwxkCdjiw.cBZ65edt94fce1R4ns4VqaShnGKg6c2q2VwjgQrxS%%2Fk; token=t.ZolH0dnGX4IhzKqZbItX; default_city_code=000002; JSESSIONID-FANG=YzhmY2Q2ZjEtMzliZS00ZmIwLTlmNjgtZTE0ZTJhMDNjNTI3; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1682302655,1683620667; Hm_lpvt_1851e6f08c8180e1e7b5e33fb40c4b08=1683620667; Hm_lvt_728857c2e6b321292b2eb422213d1609=1682302655,1683620667; Hm_lpvt_728857c2e6b321292b2eb422213d1609=1683620667; login-workerid=06045224; login-mac=CB8222B5C1a629B422347aC7597aC794014b86Cb; jjshome_sid=%s; JSESSIONID=%s; proLEYOUJIA=%s' % (
        jjshome_uuid_value, jjshome_sid_value, JSESSIONID_value, proLEYOUJIA_value)
        print('cookie1===', cookie1)

        # 若登录失败更换token
        url = "https://i.leyoujia.com/jjslogin/scanCheck"
        self.Time(2)
        payload = "rCodeToken=%s" % rCodeToken
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

        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        print(response.text)

        # 若登录失败更换token
        url = "https://i.leyoujia.com/jjslogin/scanLogin"
        self.Time(2)
        payload = "rCodeToken=%s" % rCodeToken
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

        response = requests.request("POST", url, data=payload, headers=headers, verify=False)

        print(response.text)

    def getcookie(self):
        # 通过js新开一个窗口
        js = 'window.open("https://i.leyoujia.com/attend/main/index")'
        self.browser.execute_script(js)
        time.sleep(2)
        cookie = self.browser.get_cookies()
        print('cookie1===', cookie)

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

        cookie = 'jjshome_uuid=%s; _smt_uid=; cookiesId=116347ef6ac44e45a1c414bf7b790d1b; _ga=GA1.2.1941642435.1637634248; agentCardhd_time=1; token=t.LmX27IZZvGOqM1DRudGm; prefs={}; fhListCookies=; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1640866512; Hm_lvt_728857c2e6b321292b2eb422213d1609=1640866512; gr_user_id=b4d54e60-5a65-41ea-815a-9de61463cd28; proLEYOUJIA=%s; JSESSIONID=%s; login-mac=6C-0B-84-A4-72-DD; login-workerid=06045224; jjshome_sid=%s' % (
        jjshome_uuid_value, proLEYOUJIA_value, jjshome_sid_value, JSESSIONID_value)
        print('cookie===', cookie)

        print('cookie:', cookie)
        x = {'cookie': cookie}

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
    return x


def get_sessionID(url):
    body = 'loginName=tandf&loginPass=123456'
    headers = {
        'Host': '172.16.3.233:12001',
        'Connection': 'keep-alive',
        'Content-Length': '32',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sessionID': 'null',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://172.16.3.233:12001',
        'Referer': 'http://172.16.3.233:12001/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_ga=GA1.1.1238046553.1594955626'
    }
    response = requests.request("POST", url, data=body, headers=headers)
    print(response.text)
    text = response.text
    load = json.loads(text)
    sessionID = load['msg']['sessionID']
    # print (sessionID)
    return sessionID


def get_OnlinetestPassword(url1):
    sessionID = get_sessionID(url)
    headers = {
        'Host': '172.16.3.233:12001',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sessionID': sessionID,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Origin': 'http://172.16.3.233:12001',
        'Referer': 'http://172.16.3.233:12001/portal/index',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_ga=GA1.1.1238046553.1594955626'
    }
    response = requests.request("POST", url1, headers=headers)
    print(response.text)
    text = response.text
    load = json.loads(text)
    OnlinetestPassword = load['msg']

    # print ('今日预发布环境登陆密码为：',OnlinetestPassword)
    data = OnlinetestPassword
    # data = data.encode()
    print(data)
    # with open('.\\OnlinetestPassword.txt', 'wb') as f:
    # 	f.write(data)

    # 创建md5对象并加密
    print("开始对线上密码：%s进行MD5加密......." % OnlinetestPassword)
    md5 = hashlib.md5()
    b = OnlinetestPassword.encode(encoding='utf-8')
    md5.update(b)
    pass_word = md5.hexdigest()
    print("MD5加密后为：%s" % pass_word)

    sql = "UPDATE sys_emp_pass SET pass_word = '%s';" % pass_word
    print(sql)
    db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117,
                         db='hr', charset='utf8')  # 打开数据库连接
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    cur.execute(sql)  # 使用execute方法执行SQL语句
    db.commit()  # 提交请求
    # values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
    cur.close()  # 关闭数据库连接
    print("批量修改线上测试环境登录密码为：%s" % OnlinetestPassword)

    return data


# 发送邮件函数
def Email(rs_time):
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    content = response_time + rs_time
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "1093040152@qq.com"  # 用户名
    mail_pass = "kjdwsramukzxfjda"  # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers = ['高亚静<838456406@qq.com>', 'lin@leyoujia.com<lin@leyoujia.com>', '袁猛<yuanm@leyoujia.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8')  # 文本内容
    message['From'] = '袁猛<1093040152@qq.com>'  # mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers)  # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'线上测试密码'  # 主题
    message['Subject'] = subject

    try:
        c = smtplib.SMTP()
        c.connect(mail_host, 25)  # 25 为 SMTP 端口号
        c.login(mail_user, mail_pass)  # 登录
        c.sendmail(mail_user, receivers, message.as_string())  # 发送
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
        print("Error: 无法发送邮件")


"""
1、利用消息平台发送UAT密码给相关人员
"""


def XXPT_fs(txt, title, emp_number, emp_name, Cookie):
    url = "https://i.leyoujia.com/msg/im/addTemplateInfo"
    data = {
        "belongDept": "12",
        "laterRemind": "1",
        "pushMode": "1",
        "pushWorker": "2",
        "rank": "1",
        "title": title,
        "type": "1",
        "templateContents": [{"type": "text", "value": txt}],

        "templateWorkers": [
            {"type": "1",
             "workerType": "1",
             "value": emp_number,
             "name": emp_name}
        ]
    }
    headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9",
               "Cache-Control": "no-cache",
               "Connection": "keep-alive",
               "Content-Length": "464",
               "Content-Type": "application/json; charset=UTF-8",
               "Cookie": Cookie['cookie'],
               "Host": "i.leyoujia.com",
               "Origin": "https://i.leyoujia.com",
               "Pragma": "no-cache",
               "Referer": "https://i.leyoujia.com/lyj-menu/syssetting/SYS_XXTP?submenu=sent",
               "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "cors",
               "Sec-Fetch-Site": "same-origin",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
               "X-Requested-With": "XMLHttpRequest"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print('response======', response)
    s1 = response.json()
    return s1


"""
ids:发送的人员   例：[{'06045224': '袁猛'}, {'00410622': '冉成浩'}]
title:发送的标题   
text:发送的内容
"""


def js(ids, text, title):
    Cookie = getcookies()
    print('Cookie==========', Cookie)
    for i in ids:
        emp_number = list(i.keys())[0]
        emp_name = list(i.values())[0]
        sendinfo = XXPT_fs(text, title, emp_number, emp_name, Cookie)
        print(emp_number, emp_name)


if __name__ == '__main__':
    url1 = 'http://172.16.3.233:12001/apis/back/oldSystem/PassGet'
    url = 'http://172.16.3.233:12001/privilege/front/users/login'
    rs_time = get_OnlinetestPassword(url1)
    ids = [{'06045224': '袁猛'}, {'00410622': '冉成浩'},{'00454949': '曾亮'}, {'77850920': '李宗荣'}, {'00417286': '丁凯'}, {'00401515': '甘婷'}, {'02070281': '曹燕'}, {'77850125': '林美玲'},  {'02081317': '王曼莹'}, {'06058331': '刘颖'},{'00465762': '王韶雪'}]
    # ids = [{'06045224': '袁猛'}]
    print(ids)
    text = rs_time
    title = 'UAT验收环境登陆密码'
    # Cookie =get_cookies.getcookies()
    # Cookie = os.environ['cookie']
    js(ids, text, title)

# Email(rs_time)
