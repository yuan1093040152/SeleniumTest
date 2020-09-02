#coding=utf-8
import requests,json,time


# url = 'http://127.0.0.1:9917/wlwz/inter/login/login!login.action'
# data= {'user.userCode':'s001','user.password':'000000'}
# params = {'rtype':'json'}
# ret = requests.post(url,data = data,params=params)
# print ret.text
# dict = json.loads(ret.text)
# print dict['user']['classCode']





url = 'http://127.0.0.1:9917/wlwz/inter/main/garage-manager!getGarageList.action'
data = {'garageVo.companyId': '1','garageVo.type': '2'}
params = {'rtype':'json'}
ret = requests.post(url,data = data,params=params)
dict = json.loads(ret.text)
# print dict
# print dict['list']
# print dict['list'][0]
# print dict['list'][0]['garageId']
garageId = dict['list'][0]['garageId']


# url = 'http://127.0.0.1:9917/wlwz/inter/main/garage-manager!recycleTool.action'
# data = {'garageId':garageId}
# params = {'rtype':'json'}
# ret = requests.post(url,data = data,params=params)
# dict = json.loads(ret.text)
# print dict





# url = 'http://127.0.0.1:9917/wlwz/inter/login/login!login.action'
# data= {'user.userCode':'s001','user.password':'000000'}
# params = {'rtype':'json'}
# ret = requests.post(url,data = data,params=params)
# print ret.text
# dict = json.loads(ret.text)
# print dict['user']['classCode']





# url = 'http://127.0.0.1:9917/wlwz/inter/main/garage-manager!getGarageList.action'
# data = {'garageVo.companyId': '1','garageVo.type': '2'}
# params = {'rtype':'json'}
# ret = requests.post(url,data = data,params=params)
# dict = json.loads(ret.text)
# print dict
# print dict['list']
# print dict['list'][0]
# print dict['list'][0]['garageId']
# garageId = dict['list'][0]['garageId']


# url = 'http://127.0.0.1:9917/wlwz/inter/main/garage-manager!recycleTool.action'
# data = {'garageId':garageId}
# params = {'rtype':'json'}
# ret = requests.post(url,data = data,params=params)
# dict = json.loads(ret.text)
# print dict
