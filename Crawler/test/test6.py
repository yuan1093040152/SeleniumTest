#coding=utf-8
'''
Created on 2018年7月22日

@author: kai.yangf
'''
import pymongo

import requests
headers = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
   'Cookie': 'bid=rz_cI9hRUZs; gr_user_id=1d7acee2-0287-4a57-8cea-8f8d8de9926d; _vwo_uuid_v2=DB21B1A1625E65BEBD83CEB02102CB1F2|72d82e5166152ebf715de4564ef118cd; ll="118282"; douban-fav-remind=1; __utmc=30149280; __utmc=223695111; __yadk_uid=FObf6u96PSJsXokW8o81haedZ8ZrlBF6; __utmz=30149280.1534167820.6.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1534167837.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; ps=y; dbcl2="182905276:wUYy5yjK3go"; ck=-IsS; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18290; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1534172159%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E7%2588%25B1%25E6%2583%2585%25E5%2585%25AC%25E5%25AF%2593%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.134256535.1531628836.1534167820.1534172159.7; __utmb=30149280.0.10.1534172159; __utma=223695111.1924155510.1534058560.1534167837.1534172159.3; __utmb=223695111.0.10.1534172159; _pk_id.100001.4cf6=52266675b8c2aea9.1534058560.3.1534172861.1534168875.',
}
seen_url = start_url = 'https://movie.douban.com/subject/24852545/comments?limit=20&sort=new_score&status=P&start='



def get_one_pahe(url):
    for i in range(100):
        url = seen_url + str(i*20)
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None

