#coding=utf-8
'''
Created on 2018年3月14日

@author: 唐路
'''

import urllib2,re,urlparse
from bs4 import BeautifulSoup
from re_grab import download

def get_links(html):
    webpage = re.compile('<a[^>+]href=["\'](.+?)["\']', html)
    links = webpage.find_all(html)
    return links


def shot(url):
    try:
        html = download(url)
        print html
        if not html:
            return False
        soup = BeautifulSoup(html)
        links = get_links(soup)
        for link in links:
            if  re.match(link,'/pic'):
                link = urlparse.urljoin('https://www.1109df.com',link)
                html = download(url)
                soup = BeautifulSoup(html)
                meta = soup('meta',attrs={'content':'text/html; charset=utf-8'})
                title = meta.find('title')
                print title.text
    except urllib2.URLError as e:
        print e
    return

url = 'https://www.1109df.com/pic/5/'
Boole = shot(url)
print Boole

