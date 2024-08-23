#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2024/3/19 20:07
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import requests, sys, smtplib, importlib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

importlib.reload(sys)


# sys.setdefaultencoding( "utf-8" )


def city_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    start_html = requests.get(url, headers=headers)
    demo = start_html.text
    # print (demo)
    soup = BeautifulSoup(demo, 'lxml')
    return soup
    # print soup


def tianqi():
    delete()

    with open('E:\\test\\weather.txt', 'a', encoding='UTF-8') as f:

        soup = city_url(url)

        for i in range(1, 2):
            # 查询日期和星期
            # test01 = (soup.find('div', class_="day7").find('ul', class_="week").find_all('li'))[i]
            # test011 = test01.get_text()
            # print u'日期:  %s' % test011
            # f.write(u'日期:  %s' % test011 + '\n')

            # 查询天气  soup.select_one('ul.txt.txt2')  查询有多个class值的标签
            test02 = (soup.select_one("div.day7.twty_hour").select_one('ul.txt.txt2').find_all('li'))[i]
            test022 = test02.get_text()
            # print u'天气：  %s' % test022

            # f.write(u'天气：  %s' % test022 + '\n')

            # 查询温度
            # test03 = (soup.find('div', class_="day7").find('div', class_="zxt_shuju").find_all('li'))[i]
            test03 = (soup.select_one("div.day7.twty_hour").find('div', class_="zxt_shuju").find_all('li'))[i]
            # test04 = test03.get_text()
            # 最高
            # test05 = test04[:2]
            test05 = test03.find('span').get_text()
            # print u'最高温度:  %s℃' % test05
            # f.write(u'最高温度:  %s℃' % test05 + '\n')

            # 最低
            # test06 = test04[2:]
            test06 = test03.find('b').get_text()
            # print u'最低温度:  %s℃' % test06
            # f.write(u'最低温度:  %s℃' % test06 + '\n')

            # 风向
            test07 = (soup.find_all('ul', class_="txt"))[1]
            test08 = (test07.find_all('li'))[i].get_text()
            # print u'风向:  %s' % test08
            # f.write(u'风向:  %s' % test08 + '\n')
            # f.write('----------------------------------------' + '\n')
            if test022 == u'晴':
                print(u'明天天气:%s，又是元气满满的一天，撸起袖子加油干~' % test022)
                f.write('\n' + u'明天天气:%s，又是元气满满的一天，撸起袖子加油干~' % test022 + '\n')
            elif test022 == u'雨':
                print(u'明天天气:%s，记得带伞哈~' % test022)
                f.write('\n' + u'明天天气:%s，记得带伞哈~' % test022 + '\n')
            elif test022 == u'阴':
                print(u'明天天气:%s，敢问是哪位道友在此渡劫~' % test022)
                f.write('\n' + u'明天天气:%s，敢问是哪位道友在此渡劫~' % test022 + '\n')
            elif test022 == u'多云':
                print(u'明天天气:%s，那云像极了妳甜甜的笑容~' % test022)
                f.write('\n' + u'明天天气:%s，那云像极了妳甜甜的笑容~' % test022 + '\n')
            else:
                print(u'明天天气:%s，老夫掐指一算，还是呆在家里比较香~' % test022)
                f.write('\n' + u'明天天气:%s，老夫掐指一算，还是呆在家里比较香~' % test022 + '\n')

            if int(test05) - int(test06) >= 10:
                print(u'明天温差较大，冷热交替，小心感冒流鼻涕，哈哈~')
                f.write(u'明天温差较大，冷热交替，小心感冒流鼻涕，哈哈~' + '\n')
            else:
                print(u'明天温差不大，愿妳有个好心情，开心一整天~')
                f.write(u'明天温差不大，愿妳有个好心情，开心一整天~' + '\n')

            if int(test06) >= 18:
                print(u'明天夜晚最低温度:%s℃，热的话可别踢被子哟~' % test06)
                f.write(u'明天夜晚最低温度:%s℃，热的话可别踢被子哟~' % test06 + '\n\n\n')
            else:
                print(u'明天夜晚最低温度:%s℃，请盖好被子，盖好小jiojio，我要开始讲故事了~' % test06)
                f.write(u'明天夜晚最低温度:%s℃，请盖好被子，盖好小jiojio，我要开始讲故事了~' % test06 + '\n\n\n')

        f.write(u'亲，以下是深圳未来一周的天气，请查收 ~' + '\n\n')
        for i in range(7):
            # 查询日期和星期
            test01 = (soup.select_one("div.day7.twty_hour").find('ul', class_="week").find_all('li'))[i]
            test011 = test01.get_text()
            print(u'日期:  %s' % test011)
            f.write(u'日期:  %s' % test011 + '\n')

            # 查询天气  soup.select_one('ul.txt.txt2')  查询有多个class值的标签
            test02 = (soup.select_one("div.day7.twty_hour").select_one('ul.txt.txt2').find_all('li'))[i]
            test022 = test02.get_text()
            print(u'天气：  %s' % test022)
            f.write(u'天气：  %s' % test022 + '\n')

            # 查询温度
            test03 = (soup.select_one("div.day7.twty_hour").find('div', class_="zxt_shuju").find_all('li'))[i]
            # test04 = test03.get_text()
            # 最高
            # test05 = test04[:2]
            test05 = test03.find('span').get_text()
            print(u'最高温度:  %s℃' % test05)
            f.write(u'最高温度:  %s℃' % test05 + '\n')

            # 最低
            # test06 = test04[2:]
            test06 = test03.find('b').get_text()
            print(u'最低温度:  %s℃' % test06)
            f.write(u'最低温度:  %s℃' % test06 + '\n')

            # 风向
            test07 = (soup.find_all('ul', class_="txt"))[1]

            # 加个异常判断，跳过index超出范围
            try:
                test08 = (test07.find_all('li'))[i].get_text()
            except:
                continue

            print(u'风向:  %s' % test08)
            f.write(u'风向:  %s' % test08 + '\n')
            f.write('----------------------------------------' + '\n')
        f.close()


# 清空文件内容
def delete():
    with open('E:\\test\\weather.txt', 'r+', encoding='UTF-8') as f:
        read = f.read()
        f.seek(0)
        f.truncate()
    f.close()


# 读取文件信息
def txt_info():
    with open('E:\\test\\weather.txt', 'r', encoding='UTF-8') as f:
        txt_info1 = f.read()
        # print (txt_info1)
        return txt_info1


def Email():

    content = txt_info()
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    smtp_port = 587
    mail_user = "1093040152@qq.com"  # 用户名
    mail_pass = "kjdwsramukzxfjda"  # QQ邮箱登录的授权码
    #receivers =['袁猛<1093040152@qq.com>','袁猛<1093040152@qq.com>','袁猛<1093040152@qq.com>']
    receivers = ['袁猛<1093040152@qq.com>']

    # 构造邮件内容
    subject = u'妳在看天气，而我在看妳'
    # body = content
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(mail_user)
    message['To'] = Header(','.join(receivers))
    message['Subject'] = Header(subject)
    try:
        # 连接SMTP服务器
        smtp_obj = smtplib.SMTP(mail_host, smtp_port)
        smtp_obj.starttls()  # 使用TLS加密连接
        smtp_obj.login(mail_user, mail_pass)  # 登录发件人邮箱

        # 发送邮件
        smtp_obj.sendmail(mail_user, receivers, message.as_string())
        print("邮件发送成功")

    except Exception as e:
        print("邮件发送失败:", str(e))

    finally:
        smtp_obj.quit()


if __name__ == '__main__':
    city = 'shenzhen'
    url = 'https://www.tianqi.com/%s/' % city
    print(url)
    tianqi()
    Email()
