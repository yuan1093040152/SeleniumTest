#coding=utf-8
'''
Created on 2018年3月17日

@author: 唐路
'''
import re,time,csv
import lxml.html
import lxml.cssselect
from re_grab import download
from bs4 import BeautifulSoup
import robotparser,urlparse
from link_crawler import *
from public import *




def scrape_callback(url,html):
    if re.search('/view/',url):
        fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content() for field in fields]
        write_csv(row)
    return 


class ScrapeCallBack():    
    def __init__(self):
        self.writer = csv.writer(open('G:\\Crawler\\Crawler_Csv\\countries.csv','w'))
        self.fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 
        self.writer.writerow(self.fields)
    
    def __call__(self,url,html):
        if re.search('/view',url):
            row = []
            tree = lxml.html.fromstring(html)
            for field in self.fields:
                row.append(tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content())
                self.writer.writerow(row)


send_url = 'http://example.webscraping.com/'
# send_url = 'http://example.webscraping.com/places/default/view/China-47'
link_crawler(send_url,link_regex='/(index|view)', scrape_callback= ScrapeCallBack())
