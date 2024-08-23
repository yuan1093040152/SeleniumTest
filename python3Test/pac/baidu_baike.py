#coding=utf-8
import requests,sys,smtplib
from bs4 import BeautifulSoup

def baike_all(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    start_html = requests.get(url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo, 'lxml')
    # return soup
    print (soup)



if __name__ == '__main__':
    url = 'https://www.zhihu.com/'
    baike_all(url)