#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/12/15 17:34
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

"""
多个Excel表头字段需要一致
"""

import os
import pandas as pd

def filename(path):
    filepath = os.listdir(path)
    #地址拼接
    pathlist = []
    for i in filepath:
        a = path+i
        pathlist.append(a)
    print(pathlist)
    return pathlist

def excelmarge(nowpath):
    #  合并
    li = []
    for i in filename(path):
        #加载excel并存入列表
        x = pd.read_excel(i)
        li.append(x)
    #数据合并
    marge = pd.concat(li)
    #创建写入对象
    writer = pd.ExcelWriter(path+nowpath)
    #写入表格,index行序号
    marge.to_excel(writer, '合并', index=False)
    #保存
    writer.save()

if __name__ == '__main__':
    # 读取文件下所有文件
    path = 'C:\\Users\\admin\\Desktop\\test\\'
    nowpath = '合并.xlsx'
    excelmarge(nowpath)