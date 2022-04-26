#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/4/26 16:19
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

"""
查询两个excel或者某个excel中两列数据不一致的地方
"""

import numpy as nd
import pandas as pd

dfxm=pd.read_excel(r"C:\Users\admin\Desktop\test.xlsx",sheet_name=0)

df=pd.read_excel(r"C:\Users\admin\Desktop\test.xlsx")

dept1=list(dfxm["dept"].astype(str))
dept=list(dfxm["dept1"].astype(str))
# print(list(dept))
# print(dept1)
list1=[]

for i in dept:
    if i in dept1:
        print('两边都有的分行：', i)
    else:
        list1.append(i)

#去重
aa = set(list1)

print(list(aa))

