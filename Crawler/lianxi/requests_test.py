#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''

import requests
 
# url = 'https://www.xphonecdn.com/pic/5/2018-07-09/b1b640aad8257279df85cab5ea1a3de4.jpg'
# response = requests.get(url)
# print (response.content)
# 
# with open('F:\\Crawler\\Img\\01.jpg','wb') as f:
#     f.write(response.content)
#     f.close()

# response = requests.get('http://www.jianshu.com')
# print (response.cookies)
# print (response.headers)






s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print (response.text)
























