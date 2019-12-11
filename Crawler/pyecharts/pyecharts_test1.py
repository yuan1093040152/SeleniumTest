#coding=utf-8
'''
Created on 2018年8月14日

@author: kai.yangf
'''
from pyecharts import Bar, Scatter3D
from pyecharts import Page


page = Page()         # step 1

# bar
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [100, 250, 80, 600, 200, 800]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
page.add(bar)         # step 2




page.render()        # step 3