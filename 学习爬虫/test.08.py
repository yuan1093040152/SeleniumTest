#coding=utf-8
from bs4 import BeautifulSoup
import requests,os
# pip install lxml
all_url = 'https://www.qiushibaike.com/pic/'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}  

start_html = requests.get(all_url,headers=headers) 

soup = BeautifulSoup(start_html.text,'lxml')
test1 = soup.find('div',class_="col1").find('img')['src']


path = path.strip()
isExists = os.path.exists(os.path.join("E:/TestSoftware", path))

