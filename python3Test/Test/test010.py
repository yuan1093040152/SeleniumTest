#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/7/13 16:00
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import numpy as np
import matplotlib.pyplot as plt


#X轴，Y轴数据
x = ['2022-07-08',1,2,3,4,5,6]
y = ['aa','aa',2,5,3,4.5,4]
plt.figure(figsize=(6,4)) #创建绘图对象
plt.plot(x,y,color='red',linestyle='-',marker='.',linewidth=1,label='test')   #在当前绘图对象绘图（X轴，Y轴，颜色，线条，标记，线宽度,图标签）
plt.xlabel("Time(s)") #X轴标签
plt.ylabel("Volt")  #Y轴标签
plt.title("Line plot") #图标题
plt.legend(loc="upper left") #显示图标签
plt.xticks(rotation=50)  #X轴数据展示效果
plt.show()  #显示图
# plt.savefig("line.jpg") #保存图
