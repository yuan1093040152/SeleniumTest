#coding=utf-8
'''
Created on 2018年3月15日

@author: 唐路
'''

fields = ('area','population','iso','country' ,'capital', 'continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours') 

import re,time
import lxml.html
import lxml.cssselect
from re_grab import download
from bs4 import BeautifulSoup



def re_scraper(html,fields):
    results = {}
    for field in fields:
        results[field] = re.findall('<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>'%field,html)[0]
    return results




def bs_scraper(html,fields):
    soup = BeautifulSoup(html,'html.parser')
    results = {}
    for field in fields:
        results[field] = soup.find('table').find('tr',id='places_%s__row'%field).find('td',attrs={'class':"w2p_fw"}).text
    return results

def lxml_scraper(html,fields):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in fields:
        results[field] = tree.cssselect('table>tr#places_%s__row > td.w2p_fw'%field)[0].text_content()
    return results


num_iteraions = 1000
url = 'http://example.webscraping.com/places/default/view/China-47'
html = download(url)
for name ,scraper in [('Regular expressions',re_scraper),('BeauifulSoup',bs_scraper),('Lxml',lxml_scraper)]:
    start = time.time()
    for i in range(num_iteraions):
        if scraper == re_scraper:
            re.purge()
        result = scraper(html,fields)
        assert(result['area'] == '9,596,960 square kilometres')
    end = time.time()
    print '%s: %.2f seconds'%(name,end-start)
 
# url = 'http://example.webscraping.com/places/default/view/China-47'
# html = download(url)
# # print html
# results = lxml_scraper(html,fields)
# print results






