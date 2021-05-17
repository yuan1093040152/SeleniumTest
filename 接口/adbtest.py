#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/4/25 11:23
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import os

content = os.popen("adb devices")

data = content.readlines()

for i in data[1:2]:
    print(i)

print(len(i))
print(i[-7:])
number = i[-7:].strip()
info = len(i)
if info < 2:
    print('未检测到设备，请检查是否连接手机和USB调试是否打开')
elif info > 2 and number == 'device':
    print('已连接，请选择参数开始测试')

else:
    print('未知原因，请检查驱动')