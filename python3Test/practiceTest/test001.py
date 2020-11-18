#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/17 17:57
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests
import eventlet
import time

eventlet.monkey_patch()

time_limit = 3  # set timeout time 3s
for i in range(3):
    with eventlet.Timeout(time_limit, False):
        # time.sleep(5)int('error')
        #     print('over')
        r = requests.get("https://me.csdn.net/dcrmg", verify=False)
        pr