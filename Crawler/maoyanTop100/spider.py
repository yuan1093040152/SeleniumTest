#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
import requests,re
from MongoDB import *
from selenium import webdriver
from requests.exceptions import RequestException

def chromedriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')   
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def get_one_page(driver,url):
    try:
        driver.get(url)
        html = driver.page_source
        return html
    except:
        return None

    
    
    

def parse_one_page(html):
#     print (html)
#     pettern = re.compile('<dd.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?board-img.*?src="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    pettern = re.compile('<dd.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name.*?<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pettern,html)
    movieTopList = []
    for item in items:
        movieTop ={}
        movieTop['index'] = item[0]
        movieTop['img'] = item[1]
        movieTop['title'] = item[2]
        movieTop['star'] = item[3].strip()[3:]
        movieTop['releasetime'] = item[4].strip()[5:]
        movieTop['grade'] = item[5] + item[6]
        movieTopList.append(movieTop)
    return movieTopList
        
        
    
def main(driver,url):
    html = get_one_page(driver,url)
    movieTop = parse_one_page(html)
    for movie in movieTop:
        print (movie)
        storage.insert(movie)

if __name__ == '__main__':
    driver = chromedriver()
    try:
        for i in range(10):
            base_url = 'http://maoyan.com/board/4?offset='
            url = base_url + str(i*10)
            main(driver,url)
    finally:
        driver.quit()

