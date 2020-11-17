#coding=utf-8
import requests,sys,smtplib
from bs4 import BeautifulSoup

def link_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    start_html = requests.get(url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo, 'lxml')
    # print(soup)

    link_all = soup.find_all('a',class_='contentHerf')
    # print(link_all)

    inurl = 'https://www.qiushibaike.com'
    for link in link_all:
        src = inurl+link['href']
        print(src)

        start_html_1 = requests.get(src, headers=headers)
        demo = start_html_1.text
        soup1 = BeautifulSoup(demo, 'lxml')
        print(soup1)








if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/text/'

    link_list(url)