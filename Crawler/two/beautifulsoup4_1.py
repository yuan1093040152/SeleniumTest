#coding=utf-8
'''
Created on 2018年3月14日

@author: 唐路
'''
from bs4 import BeautifulSoup
from re_grab import download
# 
broken_html = '<ul class=country><li>Area</li><li>Population</ul>'
soup = BeautifulSoup(broken_html,'html.parser')
print soup
fixed_html = soup.prettify()
print fixed_html
  
  
ul = soup.find('ul',attrs={'class':'country'})
print ul.find('li')
print ul.find_all('li')


def Soup(url):
    html = download(url)
    soup = BeautifulSoup(html)
    tr = soup.find(attrs={'id':'places_area__row'})
    td = tr.find(attrs={'class':'w2p_fw'})
    value = td.text
    print value
    return


url = 'http://example.webscraping.com/places/default/view/China-47'
# Soup(url)