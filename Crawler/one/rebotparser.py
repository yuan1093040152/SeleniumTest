#coding=utf-8
'''
Created on 2018年3月14日

@author: 唐路
'''
import robotparser
from first_one_baidu import *
from public import *

def link_crawer(send_url,link_regex):
    rp = robotparser.RobotFileParser()
    rp.set_url('http://example.webscraping.com/robots.txt')
    rp.read()
    url = 'http://example.webscraping.com'
    user = 'BadCrawler'
    crawl_queue = [send_url]
    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user,url):
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
        else:
            print False
    return



if __name__ == '__main__':
    send_url = 'http://example.webscraping.com'
    # link_regex = '/(index|view)'
    link_regex = '/places'
    url = link_crawer(send_url, link_regex)
    # writeLinks(html)
    print url

