#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''

import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException



try:
    response = requests.get('http://httpbin.org/get',timeout=0.5)
    print (response.status_code)
except ReadTimeout:
    print ('timeout')
except ConnectionError:
    print ('Connection error')
except RequestException:
    print ('error')
    