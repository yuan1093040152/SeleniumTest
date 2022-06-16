#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/6/16 14:39
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import hashlib


a = '123456'

# 创建md5对象
md5 = hashlib.md5()

# 此处必须encode
# 若写法为m.update(str)
# 报错为：Unicode-objects must be encoded before hashing,因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = a.encode(encoding='utf-8')
md5.update(b)
str_md5 = md5.hexdigest()

print('MD5加密前为 ：' + a)
print('MD5加密后为 ：' + str_md5)


