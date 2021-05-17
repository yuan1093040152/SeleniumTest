#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/4/17 11:16
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import pytest

@pytest.fixture()
def login():
    print('已调用登录')


@pytest.fixture()
def login1():
    print('已调用登录1')

@pytest.fixture()
def login2(request):
    print('已调用登录22')

@pytest.fixture()
def login3():
    print('1111111111111')
