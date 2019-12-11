# coding=utf-8
from selenium import webdriver
# from appium import webdriver
import os,time
#调动谷歌登录网址
driver = webdriver.Chrome()
url="http://123.207.86.50/company/"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.implicitly_wait(30)

#封装登录函数
def login(x):
    #点击注册
    driver.find_element_by_xpath('//*[@id="longinModule"]/div/div/div/div[1]/div/div/div/div/div[3]').click()
    time.sleep(1)
    #输入账号
    driver.find_element_by_xpath('//*[@id="longinModule"]/div/div/div/div[2]/div[2]/div/div/div[2]/input').send_keys(x)
    time.sleep(1)
    #点击发送验证码
    driver.find_element_by_xpath('//*[@id="longinModule"]/div/div/div/div[2]/div[2]/div/div/button[1]/span/span').click()
    time.sleep(2)
    #调用获取验证码函数获取验证码
    try:
        driver1 = logcat()
        print (driver1)
    except Exception as e:
        return false
        print (e)
    time.sleep(2)   
    #输入验证码 
    driver.find_element_by_xpath('//*[@id="longinModule"]/div/div/div/div[2]/div[2]/div/div/div[3]/input').send_keys(driver1)
    time.sleep(1)
    #点击注册
    driver.find_element_by_xpath('//*[@id="longinModule"]/div/div/div/div[2]/div[2]/div/div/button[2]/span').click()
    time.sleep(4)
    print ('注册成功')
    return x 


#封装获取验证码函数
#获取验证码需要连接手机并打开调试模式（重要）
def logcat():   #获取日志函数
    cmd_c = 'adb logcat -c'
    os.popen(cmd_c)         #清除以前的日志
    for i in range(30):                 #30秒没有短信日志抛ValueError
        try:
            cmd_d = 'adb logcat -d | findstr codeString'  
            value = os.popen(cmd_d).read()              #获取刚刚的短信验证码哪一行日志信息
            print (value)
            code = value.split('验证码：')[1].split('，')[0]
            print (code)
            break
        except:
            pass
        time.sleep(1)
    else:
        raise ValueError
    return code 


#输入手机号
x = '13570874427'
#调用登录函数
driver2 = login(x)
