#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/5/11 11:22
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import requests,json

url = "pl:NXXR"
print(url[-4:])


a = [{'袁猛':'06045224'},{'冉成浩':'00410622'}]

for i in a:
    print(type(list(i.keys())[0]))
    print(list(i.values())[0])