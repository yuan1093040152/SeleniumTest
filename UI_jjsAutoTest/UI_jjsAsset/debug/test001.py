#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/8 11:58
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import configparser,os



# 定义文件路径

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件拼接
CONFIG_PATH = BASEPATH + os.path.sep + 'config' + os.path.sep + 'config.ini'
print(CONFIG_PATH)



config = configparser.ConfigParser() # 类实例化
config.read(CONFIG_PATH)
value = config['user']['ipassword']
value2 = config.get('user','ipassword')
value3 = config.items('user')


print(value)
print(value2)
print(value3)




