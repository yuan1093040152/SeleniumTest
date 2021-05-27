#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/5/26 8:44
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from selenium import webdriver
from email.mime.text import MIMEText
import requests,json,urllib3,time,smtplib
import urllib.parse



class send_WX():


    def __init__(self,appToken,uids):
        self.appToken = appToken
        self.uids = uids

    def send(self):
        self.url = 'http://wxpusher.zjiecode.com/api/send/message'
        headers = {
            'Content-Type':'application/json'
        }

        body = {
            'appToken':self.appToken
            ,'content':'1231312'
            ,'summary': '666'
            ,'contentType': '1'
            ,'topicIds': ''
            ,'uids': self.uids
            ,'url': ''

        }

        response1 = requests.request('post', self.url, data=body, headers=headers, verify=False)
        print(response1.text)

appToken = 'AT_wW7eEobXR61htcs4zw6HIchK1yUaSx8L'
uids = 'UID_j0EdePPCONxX3OszmdyvwSYknX8m'

p = send_WX(appToken,uids)
p.send()



