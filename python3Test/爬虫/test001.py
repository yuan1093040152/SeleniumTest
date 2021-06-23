#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/6/22 15:36
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
from PIL import Image
path = '123.png'
path1 = '1234.png'

left = 1354-20
top = 416-20
elementWidth = 1414+20
elementHeight = 434+20
print(left,top,elementWidth,elementHeight)
picture = Image.open(path)
picture = picture.crop((left,top,elementWidth,elementHeight))
picture.save(path1)