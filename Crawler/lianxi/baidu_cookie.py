#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''

# import http.cookiejar,urllib.request
# 
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print (item.name + '=' + item.value )


from urllib import request,error


try:
    response = request.urlopen('http://yangk77ai.com/index.html')
except error.HTTPError as e:
    print (e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print (e.reason)
else:
    print ('请求成功')



