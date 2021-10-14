#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/10/14 14:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import qrcode,time
 # //调用qrcode的make()方法传入url或者想要展示的内容
img = qrcode.make('队长二百五')

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
print(now)
 # //保存
img.save("E://test//%s.png"%now)