#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/5/10 14:16
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from python3Test.Test import detection_Sensitive

text = '砂浆好的刷卡机会叼毛是的我操空间和是'
t=detection_Sensitive.Sensitive()
t.get_info(text)