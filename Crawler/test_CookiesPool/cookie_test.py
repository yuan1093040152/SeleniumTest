#coding=utf-8
from selenium import webdriver
import time,requests,json
from selenium.webdriver.chrome.options import Options

response = requests.get('http://127.0.0.1:5000/weibo/random')
print (response.text)
cookie = response.text
# cookie = json.loads(response.text)

def request(cookie):
    url = 'https://crm.winbons.com/feed/createGroup'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'crm.winbons.com',
        'Origin': 'https://crm.winbons.com',
        'Referer': 'https://crm.winbons.com/homepage',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Tingyun-Id': '8N-GQUTewUE;r=53336579',
        }
    headers['Cookie'] = cookie
    data = {
        'content': 'dsadasdadads',
        'itemTypeValue': 'hp_releaseDynamicNormal',
        'groupTypeId': '-1',
        'depId': '10000',
        }
    response = requests.post(url=url,data=data,headers=headers)
    print (response.text)

# cookievalue = login()
request(cookie)