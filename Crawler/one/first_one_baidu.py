#coding=utf-8
'''
Created on 2018年3月13日

@author: 唐路
'''


import urllib2,re
from public import *
from _weakref import proxy



def download(url,user = 'wswp',num = 2):
    print 'Download:',url
    headers = {'User-agent':user}
    request = urllib2.Request(url,headers = headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Error: ',e.reason
        html = None
        if num > 0:
            if hasattr(e,'code') and e.code >= 500:
                return download(url,num-1)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall('href="(.+?)"',sitemap)
    for link in links:
        current_url = url + link
        if 'view' in current_url:
            html = download(current_url)
            write_txt(html)
    return 


import itertools

def re_id():
    for page in itertools.count(1):  
    #itertools.count(1)代表每次+1
        url = 'http://example.webscraping.com/places/default/view/Afghanistan-%d'%page
        html = download(url)
        if html == None:
            break
        else:
            print page 
            print True
    print False
    return

def get_links(html):
    webpage_pegex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_pegex.findall(html)


def link_crawler(send_url,link_regex):
    #send_url 用来匹配url的开头
    #link_regex 用来匹配url的地址
    crawl_queue = [send_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                crawl_queue.append(link)
    return


import urlparse


def link_crawer(send_url,link_regex):
    crawl_queue = [send_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        write_txt(html)
        time.sleep(1)
        links = get_links(html)
        print links
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urlparse.urljoin(send_url,link)
                #拼接url
                seen = []
                if link not in seen:
                    seen.append(link)
                    crawl_queue.append(link)
        return crawl_queue



if __name__ == '__main__':
    send_url = 'http://example.webscraping.com'
    # link_regex = '/(index|view)'
    link_regex = '/places'
    url = link_crawer(send_url, link_regex)
    # writeLinks(html)
    print url









