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
def get_pageimg_detail(url):
    driver.get(url)
    time.sleep(1)
    source = driver.page_source
    doc = pq(source)
    title = doc('title').text()
    print (title)
    items = doc('.imageList .image-list .image-item').items()
    print (items)
    images = []
    for item in items:
        print (item)
#         pattern = re.compile('image-item".*?<a.*?href="(.*?)"',re.S)
#         image = re.search(pattern, str(item))
#         print (image)
#         
        
        value = item.find('li').text()
        print (value)
         
#         image = item.find('.image-item .image-item-inner a').attr('href')
        image = item.find('a').text()
        image = item.find('.image-item .image-item-inner a').attr('title')
#         image = item.find('a')
        print (image)
        images.append(image)
    print (images)
    


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
        get_pageimg_detail(url)
        break



if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    offset = '0'
    keyword = '街拍'
    main(offset,keyword)