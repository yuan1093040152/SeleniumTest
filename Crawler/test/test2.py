#coding=utf-8
'''
Created on 2018年7月22日

@author: kai.yangf
'''


import requests

proxy_result = requests.get("http://127.0.0.1:8080/").json()
num = proxy_result['num']
updatetime = proxy_result['updatetime']
proxy_data = proxy_result['data']
print (proxy_data)
print (len(proxy_data))
#     # 获取其中一个代理
#     one_proxy = proxy_data[0]
#     # 爬虫加上代理
#     requests.get("http://www.baidu.com",proxies={"http":one_proxy['type']+"://"+one_proxy['ip_and_port']},timeout=3)
# 获取其中一个代理
one_proxy = proxy_data[0]


headers = {'Cookie': 'SUV=007763227923609E5B3632415B173415; CXID=E43A322A65C6293DB62CD7ADD9C875CF; SUID=3FE119745E68860A5B38399800098AC2; IPLOC=CN4403; ABTEST=0|1532141521|v1; weixinIndexVisited=1; ppinf=5|1532146063|1533355663|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8Y3J0OjEwOjE1MzIxNDYwNjN8cmVmbmljazo3MjolRTglQjQlQUIlRTUlODMlQTclRTclQkElQTAlRTclQkIlOTMlRTQlQjglQUQlRUYlQkMlOEMlRTUlOEIlQkYlRTYlODklQjB8dXNlcmlkOjQ0Om85dDJsdUtaMXlYblVWZHVCZjBXcUN2VUJ4ZmNAd2VpeGluLnNvaHUuY29tfA; pprdig=rQai2B2ph9tv5yMluUfHh5L857fasTk1AfQC8vbUUPol-HVFKRPkf7I6lcwjgrUWsKpmwoTd_GFTjL8ZU5bU7lxIu1V_CZLBSWNVLPfTkfuC-p62g2DpO_4y8XyOwCdkryVYmUJSsgMsMeL0FBmuNozmj2loYkQTpj_j5LyLZAc; sgid=29-36164553-AVtSsY8FE1OUMwrSzM0DoEA; SUIR=97AB9FB6C6C3B6BFB8D96E8CC78332F8; ad=@1xlylllll2bnRuYlllllVHvhFGlllllNxXP5ZllllYlllllVFYc25@@@@@@@@@@; SNUID=99A591B8C8CCB849B60D8F78C92A377C; ppmdig=1532243919000000f3132f325489df1d96e70b37ca17c57f; sct=2; JSESSIONID=aaaTBkxmoV63C7tLPjHsw',
            'Host': 'weixin.sogou.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}



i = 1

url = 'http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page=1'
# for one_proxy in proxy_data:
#     
# 
# # 爬虫加上代理
#     try:
#         response = requests.get(url,headers=headers,allow_redirects=False,proxies={"http":one_proxy['type']+"://"+one_proxy['ip_and_port']},timeout=1.5)
#         print (response.status_code)
#         print (response.text)
#     except Exception as e:
#         print (i,' : ',e)
#     i += 1
# # 
# def get_ip():
#     with open('F:\\workspace\\Crawler\\test\\ip.txt','r') as f:
#         lines = f.readlines()
#         porxys = []
#         for line in lines:
#             porxy = line.strip()
#             porxys.append(porxy)
#         return porxys
#              
# porxys =  get_ip()   
# print (porxys)
import time
proxysList = []
porxys = ['http://62.210.51.150:80', 'http://197.220.193.137:443', 'http://165.138.225.250:8080', 'http://72.12.204.29:8080', 'http://118.98.227.230:80', 'http://61.136.163.245:3128', 'http://95.171.198.206:8080', 'http://61.5.207.102:80']
# porxys = ['http://165.138.225.250:8080', 'http://61.136.163.245:3128']
# porxys = ['http://61.136.163.245:3128']
while True:
    time.sleep(1)
    for proxy in porxys:
        print (proxy)
        try:
            proxies = {'http':proxy}
            url = 'http://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&type=2&page=1'
            response = requests.get(url,headers=headers,proxies=proxies,timeout=2)
            print (response.text)
        except Exception as e:
            print (e)
