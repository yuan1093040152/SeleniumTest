#coding=utf-8
import re
import urlparse
import urllib2
import time
import csv
from datetime import datetime
import robotparser
import Queue
from class_download import *
import lxml.html
from DiskCache_3_2 import *


def link_crawler(seed_url, link_regex=None, delay=1, max_depth=-1, max_urls=10, headers=None, user_agent='wswp', proxies=None, num_retries=1, scrape_callback=None,cache=None):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = [seed_url]
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}                            #定义seed_url市没有下载过的
    # track how many URL's have been downloaded
    num_urls = 0
    rp = get_robots(seed_url)               #判断当前代理时候可以访当前url
    D = Downlaoder(delay=delay,user_agent=user_agent,proxies=proxies,num_retries=num_retries,cache=cache)       #定义下载的类
    while crawl_queue:                              #判断是否还有url可以继续爬取
        url = crawl_queue.pop(0)                    #删除当列表的第一个值并返回
        depth = seen[url]                           #给当前的url定义第几次访问
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):           #判断当前的代理用户是否可以访问url
            html = D(url)                           #获取当前的url的html和code值
            links = []              
            if scrape_callback:                     
                links.extend(scrape_callback(url, html) or [])  #scrape_callback返回的爬取的值加在links的列表后面
            if depth != max_depth:                  #判断当前的下载次数是否等于最大下载次数
                # can still crawl further
                if link_regex:                      #判断是否有调用正则表达式
                    # filter for links matching our regular expression
#                     links.extend(link for link in get_links(html) if re.search(link_regex, link))
                    for link in get_links(html):    #遍历在url返回中html中获取的url
                        if re.search(link_regex, link):     #判断正则的文本是否在url中
                            try:
                                int(link[-1])       #判断url的最后一个字符是否是数字
                            except ValueError:
                                continue
                            if '?' in link:         #判断？是否在连接中
                                continue
                            links.append(link)      #将url添加至links中
                for link in links:                      
                    link = normalize(seed_url, link)    #判断是否已经爬过这个链接
                    # check whether already crawled this link
                    if link not in seen:                
                        seen[link] = depth + 1          #将该url的访问次数加1，避免进入死循环
                        # check link is within same domain
                        if same_domain(seed_url, link):  #判断url和seen_url是否是一个域名
                            # success! add this new link to queue
                            crawl_queue.append(link)

            # check whether have reached downloaded maximum
            num_urls += 1  
            if num_urls == max_urls:     #判断是都达到需要爬取的链接总数
                break
        else:
            print 'Blocked by robots.txt:', url


# class Throttle:
#     """Throttle downloading by sleeping between requests to same domain
#     """
#     def __init__(self, delay):
#         # amount of delay between downloads for each domain
#         self.delay = delay
#         # timestamp of when a domain was last accessed
#         self.domains = {}
#         
#         
#     def wait(self, url):
#         """Delay if have accessed this domain recently
#         """
#         domain = urlparse.urlsplit(url).netloc
#         last_accessed = self.domains.get(domain)
#         if self.delay > 0 and last_accessed is not None:
#             sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
#             if sleep_secs > 0:
#                 time.sleep(sleep_secs)
#         self.domains[domain] = datetime.now()


def scrape_callback(url,html):
    if re.search('/view/',url):
        fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content() for field in fields]
        write_csv(row)
    return 


def download(url, headers, proxy, num_retries, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                html = download(url, headers, proxy, num_retries-1, data)
        else:
            code = None
    return html


def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    link, _ = urlparse.urldefrag(link) # remove hash to avoid duplicates
    return urlparse.urljoin(seed_url, link)


def same_domain(url1, url2):
    """Return True if both URL's belong to same domain
    """
    return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc


def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(urlparse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp
        

def get_links(html):
    """Return a list of links from html 
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


def write_csv(links):
    fo = file('G:\\Crawler\\Crawler_Csv\\countries.csv','ab')
    writer = csv.writer(fo)
    writer.writerow(links)
    fo.close()
    return


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler',cache=DiskCache())
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0,num_retries=1, max_depth=-1, user_agent='GoodCrawler')

