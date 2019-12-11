#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
import requests,re,time
from multiprocessing import pool

from requests.exceptions import RequestException
from threading import Thread



def get_one_page(url):
    try:
        response = requests.get(url)
        html = response.text
        if response.status_code == 200:
            print (True)
            print (html[:5])
            return html
        else:
            return None
    except RequestException:
        return None

    
def parse_one_page(url):
    html = get_one_page(url)
    pettern = re.compile('<img.*?alt.*?src="(.*?)" />',re.S)
    items = re.findall(pettern,html)
    print (len(items))
    for item in items:
        writeIO(item)

def writeIO(item):
    filename = str(time.time()) + '.jpg'
    response = requests.get(item)
    Path = 'E:\\CrawlerImg\\' + filename
    with open(Path,'wb') as f:
        f.write(response.content)
        f.close()
        
def each_page(url):
    host = 'https://www.8484dd.com'
    html = get_one_page(url)
    pettern = re.compile('<li.*?<a.*?href="(.+?)".*?</a>',re.S)
    items = re.findall(pettern,html)
    print (len(items))
    for item in items:
        if re.match('/pic', item):
            if re.search('.html', item):
                url = host + item
                parse_one_page(url)

def each_page_value(i):
    url = 'https://www.8484dd.com/pic/5/index_'+ str(i) +'.html'
    host = 'https://www.8484dd.com'
    html = get_one_page(url)
    pettern = re.compile('<li.*?<a.*?href="(.+?)".*?</a>',re.S)
    items = re.findall(pettern,html)
    print (len(items))
    for item in items:
        if re.match('/pic', item):
            if re.search('.html', item):
                url = host + item
                parse_one_page(url)
    
    
    
def main(url):
    html = get_one_page(url)
    parse_one_page(html)

if __name__ == '__main__':
#     for i in range(2,10):
#         url = 'https://www.8484dd.com/pic/5/index_'+ str(i) +'.html'
#         each_page(url)
    Threads = []
    for i in range(2,11):
        t = Thread(target=each_page_value, args =(i,))
        Threads.append(t)
    for i in range(2,11):
        Threads[i].start()
    for i in range(2,11):
        Threads[i].join()









    
