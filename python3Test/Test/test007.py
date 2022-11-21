#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/3/10 19:22
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from sympy import *
a=10
b=1000
x= symbols('x')
print(x)

aa = solve(a+a*x+a*(x**2)+a*(x**3)+a*(x**3)+a*(x**4)+a*(x**5)+a*(x**6)+a*(x**7)-b,x)
print(aa)


#print(solve(a+a*x+a*(x**2)+a*(x**3)+a(x**3)+a(x**4)+a*(x**5)+a*(x**6)+a*(x**7)-b,x))