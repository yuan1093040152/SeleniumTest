#coding=utf-8
import json
import requests
from requests.exceptions import ConnectionError
from cookiespool.db import *


class ValidTester(object):
    def __init__(self, website='default'):
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)
    
    def test(self, username, cookies):
        raise NotImplementedError
    
    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)


class WeiboValidTester(ValidTester):
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)
    
    def test(self, username, cookies):
        print ('type: ',type(cookies))
        cookie = cookies
        print('正在测试Cookies', '用户名', username)
        print ('正在测试的cookies: ',cookies)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            print('Cookies不合法', username)
            self.cookies_db.delete(username)
            print('删除Cookies', username)
            return
        try:
            print ('进入cookie测试阶段')
            test_url = TEST_URL_MAP[self.website]
            print ('test_url: ',test_url)
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
            response = requests.post(url=test_url, headers=headers,data=data,timeout=5, allow_redirects=False)
            print ('测试的cookie数据返回: ',response.text)
            result = json.loads(response.text)
            resultCode = result['resultCode']
            if resultCode == 200:
                print('Cookies有效', username)
            else:
                print(response.status_code, response.headers)
                print('Cookies失效', username)
                self.cookies_db.delete(username)
                print('删除Cookies', username)
        except ConnectionError as e:
            print('发生异常', e.args)

if __name__ == '__main__':
    WeiboValidTester().run()