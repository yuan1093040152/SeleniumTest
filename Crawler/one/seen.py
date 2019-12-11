#coding=utf-8
'''
Created on 2018年3月17日

@author: 唐路
'''

import robotparser
from first_one_baidu import *
from public import *


def link_crawer(send_url,link_regex):
    max_depth = 2
    seen = {}
    crawl_queue = [send_url]
    seen = {send_url: 0}
    i = 1
    while crawl_queue:
        print i 
        i += 1
        url = crawl_queue.pop()
        html = download(url)
        write_txt(html)
        time.sleep(1)
        depth = seen[url]
        links = get_links(html)
        print links
        if depth != max_depth:
            for link in get_links(html):
                if re.match(link_regex,link):
                    if re.search('/(index|view)',link):
                        link = urlparse.urljoin(send_url,link)
                    #拼接url
                if link not in seen:
                    seen[link] = depth + 1
                    crawl_queue.append(link)
    return crawl_queue


if __name__ == '__main__':
    send_url = 'http://example.webscraping.com'
    # link_regex = '/(index|view)'
    link_regex = '/places'
    url = link_crawer(send_url, link_regex)
    # writeLinks(html)
    print url

