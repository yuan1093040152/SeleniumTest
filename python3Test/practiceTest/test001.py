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
from selenium import webdriver

# a = ['123','234']
# for i in a:
#     print(i)
#
# #当前时间
# def Nowtime():
#     time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#
# now = Nowtime()
# print('%s-image.png'%now)

dst_filename =time.strftime('%Y-%m-%d-%H-%M-%S')

print('/%simage.png'%dst_filename)


