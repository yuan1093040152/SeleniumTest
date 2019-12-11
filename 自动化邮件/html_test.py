#coding=utf-8
'''
Created on 2018年7月1日

@author: kai.yangf
'''
from selenium import webdriver
import time
import  smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



results = ['strattime','endtime','executionTime','listSum','passSum','Pass','fillSum','Fill','passAllSum','startPass','startFillSum','startFill']
strattime  = '2018/6/17 17:42'  
endtime = '2018/6/17 17:42'
executionTime = '0:02:08'
listSum = '3'  
passSum = '2'
Pass = '100%'
fillSum = '2'     
Fill = '100%'
passAllSum = '2'
startPass = '100%'
startFillSum = '2'
startFill = '100%'
import re
with open('F:\\Python\\PythonRead\\testhtml.txt','r', encoding='UTF-8') as f:
    lines = f.readlines()
    f.close()
with open('F:\\Python\\PythonRead\\case.html','w') as f:
    for line in lines:
        for result in results:
            if result in line:
                reppten = re.search('>(.*?)<',line).group(1)
                if reppten == result:
                    line = line.replace(reppten,eval(result))
                    f.write(line)
                    print (line.strip())
                    break
        else:
            f.write(line)

with open('F:\\Python\\PythonRead\\case.html','r') as f:
    html_txt = f.read()




def sendMail():
    print ('正在发邮件...')
    # 发送邮箱
    sender='841346559@qq.com'
    # 发送密码，即开启smtp的授权码
    psw='djuarumclzdhbeic'
    # 接收邮箱
    receiver='1325392092@qq.com'
    # 发送邮箱服务器
    smtp_server='smtp.qq.com'
    
    # 邮件正文，可编写HTML类型
    message = MIMEMultipart()
    message['From'] = Header("autotester", 'utf-8')
    message['To'] =  Header("tester", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    #邮件正文内容
    message.attach(MIMEText(html_txt, 'html', 'utf-8'))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open('testapi.csv', 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="testapi.csv"'
    message.attach(att1)
    server=smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.starttls()
    server.login(sender,psw)
    server.sendmail(sender,receiver,message.as_string())
    server.quit()

sendMail()