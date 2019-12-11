#coding=utf-8
'''
Created on 2018年7月16日

@author: Administrator
'''
import requests,re,time
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from threading import Thread


def get_page_detail(offset,keyword):
    data = {'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'cur_tab': '3',
            'from': 'search_tab'}
    seen_url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(seen_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
#             if  item.get('article_url') == None:
#                 continue
            yield item.get('article_url')
    
    

# def get_pageimg_detail(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.text
#         else:
#             return None
#     except RequestException:
#         print ('请求详情页出错: ',url)
#         return None

def get_products():
    html = driver.page_source
    doc = pq(html)
    items = doc('.m-itemlist .items .item').items()
    i = 0
    for item in items:
        print (item)
        product = {
                   'image' : item.find('.pic .img').attr('src'),
                   'price' : item.find('.price').text(),
                   'deal'  : item.find('.deal-cnt').text(),
                   'title' : item.find('.title').text(),
                   'shop'  : item.find('.shop').text(),
                   'location'  : item.find('.location').text(),
                   }
        print (product)
#         print (item)
        i += 1
    print ('current page: ',i)


# def get_pageimg_detail(url):
#     driver.get(url)
#     time.sleep(1)
#     html = driver.page_source
#     doc = pq(html) 
#     print (doc('title').text())
#     soup = BeautifulSoup(html,'lxml')
#     print (soup.head.title.string)
#     items = doc('.imageList .image-list .image-item').items()
#     for item in items:
#         print (item)
#         image = item.find('a').attr('title')
#         print (image)
#         image = item.find('.image-item .image-item-inner a').attr('title')

    
def get_pageimg_detail(url):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    title = soup.head.title.string
    items = soup.select('.imageList .image-list .image-item a')
    images = []
    for item in items:
        image = item.attrs['href']
        images.append(image)
    return images
    
def writeIO(item):
    print (item)
    filename = str(time.time()) + '.jpg'
    response = requests.get(item)
    Path = 'D:\\CrawlerImg\\jiepai\\' + filename
    with open(Path,'wb') as f:
        f.write(response.content)
        f.close()


def parse_page_detail(html):
    if html == None:
        print (False)
    else:
        print (True)
    soup = BeautifulSoup(html,'lxml')
    print (soup)
    title = soup.select('title')[0].get_text()
    pattern = re.compile('gallery: JSON.parse\("(.*?)"\)',re.S)
    result = re.search(pattern, html)
    if result:
        print (result.group(1))

    

def main(offset,keyword):
    html = get_page_detail(offset,keyword)
    for url in parse_page_index(html):
        print (url)
    for url in parse_page_index(html):
        try:
            images = get_pageimg_detail(url)
            for image in images:
                writeIO(image)
        except:
            print ('错误页: ',url)


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    keyword = '街拍'
    for i in range(8):
        main(str(i*20),keyword)
#     Threads = []
#     for i in range(8):
#         t = Thread(target=main, args =(str(i*20),keyword,))
#         Threads.append(t)
#     for i in range(8):
#         Threads[i].start()
#     for i in range(8):
#         Threads[i].join()
#     driver.quit()
#         