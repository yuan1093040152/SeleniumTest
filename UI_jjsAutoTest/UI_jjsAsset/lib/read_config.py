#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 14:35
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import configparser

from UI_jjsAutoTest.UI_jjsAsset.lib.path import CONFIG_PATH

def read_config(key,value):
    config = configparser.ConfigParser() # 类实例化
    config.read(CONFIG_PATH)
    value = config.get(key,value)
    print(value)
    return value



if __name__ == '__main__':
    read_config('url','itesturl')
