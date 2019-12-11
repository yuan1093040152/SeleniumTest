#coding=utf-8
'''
Created on 2018年7月22日

@author: kai.yangf
'''
import requests
url = 'http://down.amcdnship.com/mp4/20180731/39.mp4'
response = requests.get(url)
content = response.content
name = '长相甜美萌妹子女主播全露道具自慰秀'
Path = 'E:\\Crawler\\CrawlerVidoe\\' + name + '.mp4'
print (Path)
with open(Path,'wb') as f:
    f.write(content)
    f.close()
