#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/5/23 9:27
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import re
import urllib.request

from PIL import Image
from aip import AipOcr
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




class Login():

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
        elif u'itest' in huanjing or u'ksitest' in huanjing:
            huanjing = '172.16.16.8:31426'
        else:
            print(u'环境指定错误，默认使用itest')
            huanjing = '172.16.16.8:31426'
        print('huanjing===',huanjing)
        try:
            headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate",
                       "Connection": "keep-alive",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                       "Host": huanjing,
                       "Cookie": "_ga=GA1.1.1890888338.1580476038; HISTORY=\"com.jjshome.im.service.dubbo.NimAccidService..../governance/services/com.jjshome.im.service.dubbo.NimAccidService/providers\\.\\.\\.\\.\\.\\.com.jjshome.im.service.dubbo.INimRoomService..../governance/services/com.jjshome.im.service.dubbo.INimRoomService/providers\"",
                       "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                       "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}
            url = 'http://%s/governance/services/%s/providers' % (huanjing, interface)
            print('url =',url)
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
        print('host, port===',host, port)

        try:
            url = u'http://172.16.100.12:29998/netdubbo'
            data = {'host': host, 'port': port, 'method': method, 'interface': interface, 'param': param, 'code': 'utf-8',
                    'outputbz': False}
            print('data =',data)
            req = requests.post(url=url, data=data, timeout=5)
            print(req.text)
            print(u'调用远程服务成功。')
        except:
            print(u'乐聊通知处理出错！')





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
    # ids = ["252613", "249279","412999","419544","405984","403963","089363","171342","436614"]
    ids = ["252613"]
    hh = time.strftime('%H', time.localtime(time.time()))
    print(hh)
    if int(hh) < 12:
        info = '请知悉，影响扣分：'
    else:
        info = 'bbbb'
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)


    # (",".join(str(i) for i in WDK_name  去列表数据并用逗号分割)
    text = '1.每天检查备忘，要合格规范；2.每天检查工单中是否有需要日清的Bug和问题；3.需求评审后2天内填写完成测试方案；4.项目转测前完成研发自测用例编写并给到开发；5.测试用例需要加上必测用例。'



    Login().IMsendinfo(ids, text, info,group='im-serve-attend',url='')

    print('-------------------end!-------------------')





