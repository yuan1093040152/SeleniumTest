#coding=utf-8

import requests,sys,smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding( "utf-8" )

city = 'shenzhen'
url = 'https://www.tianqi.com/%s/' % city

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
start_html = requests.get(url,headers=headers)
demo = start_html.text
# print (demo)
soup = BeautifulSoup(demo,'lxml')




for i in range(1,2):
    # 查询日期和星期
    test01 = (soup.find('div', class_="day7").find('ul', class_="week").find_all('li'))[i]
    test011 = test01.get_text()
    print u'日期:  %s' % test011
    # f.write(u'日期:  %s' % test011 + '\n')

    # 查询天气  soup.select_one('ul.txt.txt2')  查询有多个class值的标签
    test02 = (soup.find('div', class_="day7").select_one('ul.txt.txt2').find_all('li'))[i]
    test022 = test02.get_text()
    print u'天气：  %s' % test022

    # f.write(u'天气：  %s' % test022 + '\n')

    # 查询温度
    test03 = (soup.find('div', class_="day7").find('div', class_="zxt_shuju").find_all('li'))[i]
    test04 = test03.get_text()
    # 最高
    test05 = test04[:2]
    print u'最高温度:  %s℃' % test05
    # f.write(u'最高温度:  %s℃' % test05 + '\n')

    # 最低
    test06 = test04[2:]
    print u'最低温度:  %s℃' % test06
    # f.write(u'最低温度:  %s℃' % test06 + '\n')

    # 风向
    test07 = (soup.find_all('ul', class_="txt"))[1]
    test08 = (test07.find_all('li'))[i].get_text()
    print u'风向:  %s' % test08
    # f.write(u'风向:  %s' % test08 + '\n')
    # f.write('----------------------------------------' + '\n')
    if test022==u'晴':
        print u'明天天气:%s，请注意防晒哟~'%test022
    elif test022==u'雨':
        print u'明天天气:%s，记得带伞哈~'%test022
    else:
        print u'明天天气:%s，注意天气变化~'%test022

    if int(test05)-int(test06)>=10:
        print u'明天温差较大，冷热交替，小心感冒流鼻涕，哈哈~'
    else:
        print u'明天温差不大，适合晒太阳，记得出来走走，赶走霉运~'

    if int(test06)>=18:
        print u'明天夜晚最低温度:%s℃，可根据实际情况决定被子的厚度~' %test06
    else:
        print u'明天夜晚最低温度:%s℃，请盖好被子，盖好小jiojio，可别感冒了哟~' %test06




#12月12日星期四 晴 24 14 东风

