#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/6/28 17:24
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import base64,hashlib
import json

from Crypto.Cipher import AES
import binascii
from Crypto.Util.Padding import pad

aa = "0DIGbxUpV2a8TQTf6l4kiKTtrnNaRI1qcMPLxXma82ix0dUGGqNeCE4eYG1ifS8xWL6DR0NHKmflYgcsmW/XZ2MROaTxKQbXq3yLcWZqc8pKcmJbGVhcSXY0mDT5MsmcMCYgti1NJ0WUOHU2Zv6WIP//Q4AstV7/6yBHdFo6UJTGkRmddGAGxO4jdIciDy8vmGk6ot3cCa6GKYfJIhn4/cPXsTkjLY+OQa7BIUsye8+UgjyuiOJx8bMSyWu/FnCK6awaKVLAYdUceayuEvizT4zzGdhDLV+YjqJu7nITL5IupBXSbF5Q4lQO6glviPFZEcKM9RdlPcMhsROzPVtDZswrC7mLphcX5vrZypjmeXdnaP8VfLN7I2xfSozWp5cGZxheCNTnVgX7ayhkHjiBVQoEeuUeESYYlIH0pyJyGOI7uF79e4+jUS2OqNuOlNEg4HSBkX59HggXwiu+3yKsZ/Mfrfhm46VPbWqXHiGRiyXWKnWZd1L//KD927SFpM5UgfP8etVxDjn8tNKKK4kN0FWcYMUBbLd0mQrL8QWAihay2yvpowTlgWZPga4Cr464QRrrj0CJI9lvO1ej3THKTr3K89gWGlzapQqnW+Ot+9sN7PozUQIePBCyVG6myWXcVoTGO2YTQ/TVxvty7YNwZHyMycV7DZUim8HmcMvp/RiAwaY2IOa80bnxWIfFcTnMaGUio2nyB1SX2QPrfg/47OtYkvI+FP0oDIhDhb87+hEdLJ+11LaTUZPIVO2b2d8N7biVGafJLUU2p3NpGuuGdoPYgHLmcXvRGMdI1wxoaUuhW7e1XgSc87qJOG9xViYyJ5ec+yiECDHq8Z91nEvgC1evfPYETY2XtMp3eNSgg5EqFQBMjEYK+z9v92+fObZBmiVqEk+eMgBh98/XOXJFLRnSWQIOFgiuRuCtgUMRX4myo8X+9h8m1f6UENWHV4r+H1qLuNiLnBiu0E/dSaOinSMzVzpG3yzydTwWWtx5W/lgQOFQz5fJTBfj8QNi9+VsZBEe65m93kt5etClJc3FZzesK0R6h0oG67EhQi+dOCmbDE+f3C9uC9u7p+DLvp+sP1oqqu4klwMf/hrcdMwXnwL7rPPTMonXU7Cv4RpNKRu21YIO33JJOM6gdIXedma7PsuV4KVOYazp08yj1fIOv6kgnM4/nI5qDtV4H3zYLc269uAhGa1kg0lO8lAFCXHm3AGKg6agdGahv0aOCtZh77r0gsr9FeZANNMAGb5HtGfpYKixO9PP/I2u4mHVfcNCk1Vs/wvUiTAwAWeUwFHxrvPm9biGJ+Wrjk1M7Gwxorc69rBxmp/XqqRroGUpECS8hAI5M+BLaYp1hDIXk9nUlHR2USpVRkaiLDOLDGmU7af1l3QnZ57r3kpnyTyJY+cYlcuTeDeJmjNtRSsBymlho7Ls4QKSKOf4it+wq7dLoQCroDbdRX+eEibKJe6rrnFOUb1ws3uZPKzygdEFC86XAD5doYVzRCNdSdIxJscRmNcXsrMTXLLRsCsTEF11DWT4jZId1r3nX2EtWx4dfg/bjqkWvTX88WdjIUnIBUJX4nRGH5OItrYrMil8azy3MoMPNxGvzh1Eb6F70EBt+lBOy5oCYHPoaTFaA213Uzldn8mITiL5k4S6tTPpsGdoOEpezMuB69vtW115mP8UgGzo3Lx9ycBQJm9tc6suYCfU4JQN+HY1+DH6QGji099V0E9r2vyqg8qYYB5yjcGL/qLAqvZH1Q0+RZ8Ye9K6jtywIMWwdU3o1s9PRdhoFV5LbZhEw4xBFeC0R1vfh72PyE1I1w=="

bb = "yjGG1V9JYO4/ezGJw8yY3lm390MgKwDjHV1jxZUz+/8="

password = 'ODcyYTUxNGM1N2M2'

# class EncryptDate:
#     def __init__(self, key):
#         # 初始化密钥
#         self.key = key
#         # 初始化数据块大小
#         self.length = AES.block_size
#         # 初始化AES,ECB模式的实例
#         self.aes = AES.new(self.key.encode("utf-8"), AES.MODE_ECB)
#         # 截断函数，去除填充的字符
#         self.unpad = lambda date: date[0:-ord(date[-1])]

    # def fill_method(self, aes_str):
    #     '''pkcs7补全'''
    #     pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    #
    #     return pad_pkcs7
    #
    # def encrypt(self, encrData):
    #     # 加密函数,使用pkcs7补全
    #     res = self.aes.encrypt(self.fill_method(encrData))
    #     # 转换为base64
    #     msg = str(base64.b64encode(res), encoding="utf-8")
    #
    #     return msg

    # def decrypt(self, decrData):
    #     # base64解码
    #     res = base64.decodebytes(decrData.encode("utf-8"))
    #     # 解密函数
    #     msg = self.aes.decrypt(res).decode("utf-8")
    #
    #     return self.unpad(msg)



def xx(aa):
    # 定义AES,ECB模式
    aes = AES.new(password.encode("utf-8"), AES.MODE_ECB)
    #截断函数，去除填充的字符
    unpad = lambda date: date[0:-ord(date[-1])]
    # base64解码
    res = base64.decodebytes(aa.encode("utf-8"))
    # 解密函数
    msg = aes.decrypt(res).decode("utf-8")

    dd = unpad(msg)
    print(type(dd))
    # print(dd[1]['list'])
    ee = json.loads(dd)
    return ee
    print(ee)
    print(ee['data']['list'][0]['authStatusStrForXcx'])

# print(xx(aa))



a = ''

b = json.dumps(a)
print(b)

# if __name__ == '__main__':
    # key的长度需要补长(16倍数),补全方式根据情况而定,未补齐会报错
    # key字符长度决定加密结果,长度16：加密结果AES(128),长度32：结果就是AES(256)
    # eg = EncryptDate("ODcyYTUxNGM1N2M2")
    # # 加密字符串长同样需要16倍数：需注意,不过代码中pad()方法里，帮助实现了补全（补全方式就是pkcs7）
    # # en = eg.encrypt(aa)
    # de = eg.decrypt(aa)
    # # print(f"加密结果：{en}")
    # print(f"解密结果：{de}")

