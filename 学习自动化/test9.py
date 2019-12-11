# coding=utf-8
from appium import webdriver
import os,time
def logcat():   #获取日志函数
    cmd_c = 'adb logcat -c'
    os.popen(cmd_c)         #清除以前的日志
    for i in range(30):                 #30秒没有短信日志抛ValueError
        try:
            cmd_d = 'adb logcat -d | findstr codeString'  
            value = os.popen(cmd_d).read()              #获取刚刚的短信验证码哪一行日志信息
            print (value)
            code = value.split('验证码：')[1]#.split('，')[0]
            print (code)
            break
        except:
            pass
        time.sleep(1)
    else:
        raise ValueError
    return code 
driver1 = logcat()
