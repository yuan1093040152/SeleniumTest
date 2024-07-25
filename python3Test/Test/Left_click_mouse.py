#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2024/4/23 16:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释


模拟鼠标左击
"""

import pyautogui,time

time.sleep(5)
#获取鼠标的位置
mouse_position = pyautogui.position()
for i in range(1,30):
    time.sleep(1)
    #点击左键
    pyautogui.mouseDown(mouse_position)
    #松开左键
    pyautogui.mouseUp(mouse_position)
    print(i)
