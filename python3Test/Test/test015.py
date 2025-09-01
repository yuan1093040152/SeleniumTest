#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2025/3/24 11:21
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import hmac
import hashlib,time


res = 'eanq1t'

# MD5加密
def encryptionMD5(res):
    md5_hash = hashlib.md5()
    md5_hash.update(res.encode('utf-8'))
    md5_hex = md5_hash.hexdigest()
    return md5_hex


# 获取当前时间戳（秒级）
def timeStamp():
    timestamp = time.time()
    return int(timestamp)




# 示例
data = {"mac" : "5e:b5:9b:44:88:26",
  "mobileNo" : "",
  "timestamp" : timeStamp(),
  "passwordv2" : encryptionMD5(res),
  "appVer" : "6.4.3.1",
  "phoneBrand" : "iPhone",
  "appType" : "2",
  "loginAddr" : "广东省深圳市福田区八卦四路52-1号",
  "password" : encryptionMD5(res),
  "imei" : "0d7684b2e0d7869be91d2a039cb216ae22bfc638",
  "typ" : "密码",
  "username" : "P2Vi10000Syz",
  "lat" : "22.57012",
  "mobileInfo" : "0d7684b2e0d7869be91d2a039cb216ae22bfc638",
  "phoneModel" : "iPhone 12",
  "lng" : "114.1052",
  "ipStr" : "192.168.1.121"}

class LoginUtils:
    HMAC_SHA1 = "sha1"
    CHARSET_NAME_UTF8 = "utf-8"
    DIGITAL = "0123456789ABCDEF"

    @staticmethod
    def hmac_sha1(datas, key):
        """ 计算 HMAC-SHA1 """
        mac = hmac.new(key, digestmod=hashlib.sha1)
        for data in datas:
            mac.update(data.encode(LoginUtils.CHARSET_NAME_UTF8))
        return mac.digest()

    @staticmethod
    def encode_hex_str(byte_array):
        """ 将字节数组转换为十六进制字符串 """
        if byte_array is None:
            return None
        return ''.join(f"{b:02X}" for b in byte_array)

    @staticmethod
    def to_bytes(string):
        """ 将字符串转换为 UTF-8 字节数组 """
        return string.encode(LoginUtils.CHARSET_NAME_UTF8) if string else None

    @staticmethod
    def get_signature_str(data_map):
        """ 计算签名字符串 """
        param_value_list = [f"{k}{v}" for k, v in data_map.items()]
        print('param_value_list====',param_value_list)
        param_value_list.sort()
        datas = param_value_list
        signature = LoginUtils.hmac_sha1(datas, LoginUtils.to_bytes("~leyoujia&applogin#$%"))

        print(LoginUtils.encode_hex_str(signature))
        return LoginUtils.encode_hex_str(signature)

aa = LoginUtils.get_signature_str(data)
data["signature"]=aa
print(data)


# timestamp = time.time()
# print("当前时间戳（秒级）:", timestamp)
# print("当前时间戳（秒级）:", int(timestamp))



