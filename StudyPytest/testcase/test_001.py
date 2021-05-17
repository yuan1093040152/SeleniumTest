#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/4/17 10:05
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import pytest

pytest.mark.usefixtures('login2')
class TestCase():
    def setup_class(self):
        self.a ='123'
        print('setup_class：所有用例执行前执行一次')

    def teardown_class(self):
        print('teardown_class:所有用例结束后执行一次')

    def setup(self):
        print('setup:每个用例执行前都会执行一次')

    def teardown(self):
        print('teardown:每个用例结束后都会执行一次')

    def setup_method(self):
        print('setup_method:每个用例执行前都会执行一次')

    def teardown_method(self):
        print('teardown_mothod:每个用例结束后都会执行一次')


    def test_one(self):
        b = self.a
        print('b========',b)
        print('测试1')

    def test_two(self,login):
        print('测试2,调用conftest.py文件配置的login装饰器 ')

    def test_three(self, login1):
        print('测试2,调用conftest.py文件配置的login1装饰器 ')

    def test_four(self):
        print('测试4')


if __name__ == '__main__':
    pytest.main(['-s','test_001.py'])