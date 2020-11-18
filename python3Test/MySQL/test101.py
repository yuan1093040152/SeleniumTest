#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/11/18 17:45
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import uuid,MySQLdb,time,argparse


#获取jenkins传递过来的参数
parser=argparse.ArgumentParser()
print('parser=',parser)
parser.add_argument("emp_number")
args=parser.parse_args()
print('args=',args)
param=vars(args)
print('param=',param)
emp_number = param['emp_number']
print(emp_number)




