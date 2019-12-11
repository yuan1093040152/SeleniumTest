#coding=utf-8
'''
Created on 2018年7月21日

@author: kai.yangf
'''
import requests
from requests.exceptions import ConnectionError,RequestException
from urllib.parse import urlencode
from pyquery import PyQuery as pq

proxy_pool_url = 'http://123.207.35.36:5010/get/'

proxy = None
count_max = 5



headers = {'Cookie': 'SUV=007763227923609E5B3632415B173415; CXID=E43A322A65C6293DB62CD7ADD9C875CF; SUID=3FE119745E68860A5B38399800098AC2; IPLOC=CN4403; ABTEST=0|1532141521|v1; weixinIndexVisited=1; ppinf=5|1532146063|1533355663|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8Y3J0OjEwOjE1MzIxNDYwNjN8cmVmbmljazo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8dXNlcmlkOjQ0Om85dDJsdUtaMXlYblVWZHVCZjBXcUN2VUJ4ZmNAd2VpeGluLnNvaHUuY29tfA; pprdig=rQai2B2ph9tv5yMluUfHh5L857fasTk1AfQC8vbUUPol-HVFKRPkf7I6lcwjgrUWsKpmwoTd_GFTjL8ZU5bU7lxIu1V_CZLBSWNVLPfTkfuC-p62g2DpO_4y8XyOwCdkryVYmUJSsgMsMeL0FBmuNozmj2loYkQTpj_j5LyLZAc; sgid=29-36164553-AVtSsY8FE1OUMwrSzM0DoEA; SUIR=97AB9FB6C6C3B6BFB8D96E8CC78332F8; ad=@1xlylllll2bnRuYlllllVHvhFGlllllNxXP5ZllllYlllllVFYc25@@@@@@@@@@; SNUID=99A591B8C8CCB849B60D8F78C92A377C; ppmdig=1532243919000000f3132f325489df1d96e70b37ca17c57f; sct=2; JSESSIONID=aaaTBkxmoV63C7tLPjHsw',
            'Host': 'weixin.sogou.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

def get_ip():
    with open('F:\\workspace\\Crawler\\test\\ip.txt','r') as f:
        lines = f.readlines()
        porxys = []
        for line in lines:
            porxy = line.strip()
            porxys.append(porxy)
        return porxys
            
porxys =  get_ip()   


def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None


def get_html(url,count=1):
    global proxy
    global porxys
    print ('porxys:',len(porxys))
    try:
        print (url)
        if proxy:
            proxies = {'http':'http://' + proxy,'https':'http://' + proxy}
            response = requests.get(url,allow_redirects=False,headers=headers,proxies=proxies)
        else:
            response = requests.get(url,allow_redirects=False,headers=headers)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 302:
            print ('302')
            proxy = porxys.pop()
            if proxy:
                print ('获取了一个代理')
                return get_html(url)
        else:
            print ('访问错误')
            return None
    except ConnectionError:
        print ('连接错误')
        count += 1
        proxy = porxys.pop()
        return get_html(url,count)

def get_index(page,keywrod='风景'):
    seen_url = 'http://weixin.sogou.com/weixin'
    data = {'query': keywrod,'type': '2','page': page}
    url = seen_url + '?' + urlencode(data)
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('herf')

def main():
    for page in range(1,100):
        print (page)
        html = get_index(page)
        print (html)
        if html:
            urls = parse_index(html)
            for url in urls:
                print (url)


if __name__ == '__main__':
    main()
    
    
    
    