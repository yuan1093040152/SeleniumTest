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





def sendMail():
    print ('正在发邮件...')
    # 发送邮箱
    sender='841346559@qq.com'
    # 发送密码，即开启smtp的授权码
    psw='djuarumclzdhbeic'
    # 接收邮箱
    receiver='1719422952@qq.com'
    # 发送邮箱服务器
    smtp_server='smtp.qq.com'
    
    # 邮件正文，可编写HTML类型
    message = MIMEMultipart()
    message['From'] = Header('autotest <%s>'%sender)
    message['To'] =  Header("tester<%s>"%receiver)
    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')
    message.attach(MIMEText('hello, send by Python...', 'plain', 'utf-8'))
    #邮件正文内容\
    server=smtplib.SMTP(smtp_server)
    server.set_debuglevel(1)
    server.starttls()
    server.login(sender,psw)
    server.sendmail(sender,receiver,message.as_string())
    server.quit()

sendMail()