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
import robotparser,urlparse
from public import *


fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 

# def link_crawler(url,html,fields,):
#     links = []
#     if scrape_Callback:
#         links.extend(scrape_callback(url,html,fields) or [])
#     return



def get_links(html):
    webpage_pegex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_pegex.findall(html)


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
            write_txt(html)
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



def scrape_callback(url,html):
    if re.search('/view/',url):
        print url
        tree = lxml.html.fromstring(html)
        fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 
        row = [tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content() for field in fields]
        print url
        print row
        write_csv(row)
    return 


if __name__ == '__main__':
#     send_url = 'http://example.webscraping.com/places/default/view/China-47'
#     html = download(url)
#     link_crawler(url,html,fields)
    send_url = 'http://example.webscraping.com'
    link_regex = '/(index|view)'
    link_crawer(send_url,link_regex)

        