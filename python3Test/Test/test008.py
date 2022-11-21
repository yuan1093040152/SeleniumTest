#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/6/28 17:16
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import base64,json
from Crypto.Cipher import AES

aa = "0DIGbxUpV2a8TQTf6l4kiKTtrnNaRI1qcMPLxXma82ix0dUGGqNeCE4eYG1ifS8xWL6DR0NHKmflYgcsmW/XZ2MROaTxKQbXq3yLcWZqc8pKcmJbGVhcSXY0mDT5MsmcMCYgti1NJ0WUOHU2Zv6WIP//Q4AstV7/6yBHdFo6UJTGkRmddGAGxO4jdIciDy8vmGk6ot3cCa6GKYfJIhn4/cPXsTkjLY+OQa7BIUsye8+UgjyuiOJx8bMSyWu/FnCK6awaKVLAYdUceayuEvizT4zzGdhDLV+YjqJu7nITL5IupBXSbF5Q4lQO6glviPFZEcKM9RdlPcMhsROzPVtDZswrC7mLphcX5vrZypjmeXdnaP8VfLN7I2xfSozWp5cGZxheCNTnVgX7ayhkHjiBVQoEeuUeESYYlIH0pyJyGOI7uF79e4+jUS2OqNuOlNEg4HSBkX59HggXwiu+3yKsZ/Mfrfhm46VPbWqXHiGRiyXWKnWZd1L//KD927SFpM5UgfP8etVxDjn8tNKKK4kN0FWcYMUBbLd0mQrL8QWAihay2yvpowTlgWZPga4Cr464QRrrj0CJI9lvO1ej3THKTr3K89gWGlzapQqnW+Ot+9sN7PozUQIePBCyVG6myWXcVoTGO2YTQ/TVxvty7YNwZHyMycV7DZUim8HmcMvp/RiAwaY2IOa80bnxWIfFcTnMaGUio2nyB1SX2QPrfg/47OtYkvI+FP0oDIhDhb87+hEdLJ+11LaTUZPIVO2b2d8N7biVGafJLUU2p3NpGuuGdoPYgHLmcXvRGMdI1wxoaUuhW7e1XgSc87qJOG9xViYyJ5ec+yiECDHq8Z91nEvgC1evfPYETY2XtMp3eNSgg5EqFQBMjEYK+z9v92+fObZBmiVqEk+eMgBh98/XOXJFLRnSWQIOFgiuRuCtgUMRX4myo8X+9h8m1f6UENWHV4r+H1qLuNiLnBiu0E/dSaOinSMzVzpG3yzydTwWWtx5W/lgQOFQz5fJTBfj8QNi9+VsZBEe65m93kt5etClJc3FZzesK0R6h0oG67EhQi+dOCmbDE+f3C9uC9u7p+DLvp+sP1oqqu4klwMf/hrcdMwXnwL7rPPTMonXU7Cv4RpNKRu21YIO33JJOM6gdIXedma7PsuV4KVOYazp08yj1fIOv6kgnM4/nI5qDtV4H3zYLc269uAhGa1kg0lO8lAFCXHm3AGKg6agdGahv0aOCtZh77r0gsr9FeZANNMAGb5HtGfpYKixO9PP/I2u4mHVfcNCk1Vs/wvUiTAwAWeUwFHxrvPm9biGJ+Wrjk1M7Gwxorc69rBxmp/XqqRroGUpECS8hAI5M+BLaYp1hDIXk9nUlHR2USpVRkaiLDOLDGmU7af1l3QnZ57r3kpnyTyJY+cYlcuTeDeJmjNtRSsBymlho7Ls4QKSKOf4it+wq7dLoQCroDbdRX+eEibKJe6rrnFOUb1ws3uZPKzygdEFC86XAD5doYVzRCNdSdIxJscRmNcXsrMTXLLRsCsTEF11DWT4jZId1r3nX2EtWx4dfg/bjqkWvTX88WdjIUnIBUJX4nRGH5OItrYrMil8azy3MoMPNxGvzh1Eb6F70EBt+lBOy5oCYHPoaTFaA213Uzldn8mITiL5k4S6tTPpsGdoOEpezMuB69vtW115mP8UgGzo3Lx9ycBQJm9tc6suYCfU4JQN+HY1+DH6QGji099V0E9r2vyqg8qYYB5yjcGL/qLAqvZH1Q0+RZ8Ye9K6jtywIMWwdU3o1s9PRdhoFV5LbZhEw4xBFeC0R1vfh72PyE1I1w=="


def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)

# 解密方法
def decrypt_oralce(text, key):
    # 秘钥
    key = key
    # 密文
    text = text
    # 初始化加密器
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    # 优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    # 执行解密密并转码返回str
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    # print(decrypted_text)
    return decrypted_text



def teardown_hooks_respon(res):
    # 秘钥
    key = 'ODcyYTUxNGM1N2M2'
    res = decrypt_oralce(res, key)
    b = json.dumps(res)
    d = json.loads(b.replace('\\u0004', ''))
    res = json.loads(d)
    return res


teardown_hooks_respon(aa)
