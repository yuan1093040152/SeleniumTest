#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2024/3/19 20:31
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import smtplib

try:
    server1 = smtplib.SMTP('smtp.qq.com', 587)
    server1.ehlo()
    server1.starttls()
    server1.ehlo()
    server1.login("1093040152@qq.com", "kjdwsramukzxfjda")

    # 发送邮件的代码
    server1.sendmail('from@example.com', 'to@example.com', 'message')

except smtplib.SMTPException as e:
    print('Error: ', e)
finally:
    server1.quit()
