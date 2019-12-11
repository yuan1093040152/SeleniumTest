#coding=utf-8
'''
Created on 2018年3月17日

@author: 唐路
'''
import re,time
import lxml.html
import lxml.cssselect
from re_grab import download
from bs4 import BeautifulSoup
from callback_1 import *
import csv
from rebotparser import link_crawer


fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 

def link_crawler(url,html,scrape_callback = None):
    links = []
    if scrape_callback:
        links.extent(scrape_callback(url,html) or [])
    return

def link_crawer(send_url,link_regex):
    rp = robotparser.RobotFileParser()
    rp.set_url('http://example.webscraping.com/robots.txt')
    rp.read()
    url = 'http://example.webscraping.com'
    user = 'BadCrawler'
    crawl_queue = [send_url]
    while crawl_queue:
        print crawl_queue
        url = crawl_queue.pop(0)
        if rp.can_fetch(user,url):
            html = download(url)
            write_a(html)
            links = []
            if scrape_callback:
                print url
                links.extend(scrape_callback(url, html) or [])
            print links
            print get_links(html)
            for link in get_links(html):
                if re.search(link_regex,link):
                    link = urlparse.urljoin(send_url,link)
                    #拼接url
                    seen = []
                    if link not in seen:
                        seen.append(link)
                        crawl_queue.append(link)
        else:
            print False
    return



class ScrapeCallBack():    
    def __init__(self):
        self.writer = csv.writer(open('G:\\Crawler\\Crawler_Csv\\countries.csv','w'))
        self.fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 
        self.writer.writerow(self.fields)
    
    def __call__(self,url,html):
        if re.search('/(index|view)',url):
            row = []
            tree = lxml.html.fromstring(html)
            for field in self.fields:
                row.append(tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content())
                self.writer.writerow(row)


html = 'http://example.webscraping.com'
link_crawer('http://example.webscraping.com/',link_regex = '/(index|view)')

