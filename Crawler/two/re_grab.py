#coding=utf-8
'''
Created on 2018年3月14日

@author: 唐路
'''
import re,urllib2



def download(url,user = 'wswp',num = 2):
    print 'Download:',url
    headers = {'User-agent':user}
    request = urllib2.Request(url,headers = headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Error: ',e.reason
        html = None
        if num > 0:
            if hasattr(e,'code') and e.code >= 500:
                return download(url,num-1)
    return html

if __name__ == '__main__':
    url = 'http://example.webscraping.com/places/default/view/China-47'
    html = download(url)
    sub = '<tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.+?)</td>'
    values  = re.findall(sub,html)
    print values
    sub = '<tr id="places_area__row">.+?<td class=["\']w2p_fw["\']>(.+?)</td>'
    values  = re.findall(sub,html)
    print values



