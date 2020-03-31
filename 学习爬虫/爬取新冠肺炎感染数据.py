#coding=utf-8
import requests,sys,smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText


url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab4'


def city_url(url):
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    #verify=False 解决报SSL错误
    start_html = requests.get(url,headers=headers,verify=False)
    # start_html.encoding = start_html.apparent_encoding
    demo = start_html.text
    # print (demo)

    soup = BeautifulSoup(demo,'lxml')
    print (soup)
    # lists = soup.find_all('div')
    lists = soup.find_all(id="wx_pic")
    print ('---------------------------------------------')
    print (lists)

soup = city_url(url)







# def shuju():
#
#     soup = city_url(url)
#     print (soup)
#
#     lists = soup.find('div',class_="epidemic-wrap")
#     # lists = info.find_all(class_="total none")
#     print ('---------------------------------------------')
#     print (lists)
#     # info = lists.find_all('div')
#     # print (info)








# shuju()



