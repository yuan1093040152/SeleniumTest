#coding=utf-8
'''
Created on 2018年7月22日

@author: kai.yangf
'''
import requests
from requests.exceptions import RequestException
# 请求API，并解析json成dictionary
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
i = 1
proxieList = []
for one_proxy in proxy_data:
    
# 爬虫加上代理
    try:
        response = requests.get("http://www.baidu.com",allow_redirects=False,proxies={"http":one_proxy['type']+"://"+one_proxy['ip_and_port']},timeout=1.5)
        print (response.status_code)
        print (response.text)
        proxieList.append(one_proxy['type']+"://"+one_proxy['ip_and_port'])
        print (proxieList)
    except Exception as e:
        print (i,' : ',e)
    i += 1
print (proxieList)