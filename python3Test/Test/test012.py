#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/2/23 19:13
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

global wechat_lock
wechat_lock = Lock()

# 这里可以设置UIDS, 多个人可同时接收 [袁猛，李良，蔡姻，张斯杰，罗柳,王凯]
# UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m','UID_7zDNlQLoP6BwAJFJ6dRCuy9EQ1fp','UID_dxNzj6aupA6Q4QZrDkwmCcDLMX2e','UID_nSMBON6ECkBvdpOC3QeUfIUb7tJX','UID_pyB3i43mzt2LctecgCBZWBz035GZ','UID_IJVLOOwS4AtmaaydQzjBPoQUeBw0']
UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m']

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

text = '通知：'
send_wx_msg(text)