#coding=utf-8
import requests,json

def get_sessionID(url):
	body = 'loginName=tandf&loginPass=123456'
	headers = {
	'Host':'172.16.4.223:12001',
	'Connection': 'keep-alive',
	'Content-Length': '32',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With': 'XMLHttpRequest',
	'sessionID': 'null',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Origin': 'http://172.16.4.223:12001',
	'Referer': 'http://172.16.4.223:12001/',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': '_ga=GA1.1.1238046553.1594955626'	
	}
	response = requests.request("POST", url, data=body, headers=headers)
	print (response.text)
	text = response.text
	load = json.loads(text)
	sessionID = load['msg']['sessionID']
	# print (sessionID)
	return sessionID


def get_OnlinetestPassword(url1):
	sessionID = get_sessionID(url)
	headers = {
	'Host': '172.16.4.223:12001',
	'Connection': 'keep-alive',
	'Content-Length': '0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With':'XMLHttpRequest',
	'sessionID':sessionID ,
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	'Origin': 'http://172.16.4.223:12001',
	'Referer': 'http://172.16.4.223:12001/portal/index',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': '_ga=GA1.1.1238046553.1594955626'
	}
	response = requests.request("POST", url1,headers=headers)
	print (response.text)
	text = response.text
	load = json.loads(text)
	OnlinetestPassword = load['msg']

	# print ('今日预发布环境登陆密码为：',OnlinetestPassword)
	data = '今日预发布环境登陆密码为：\r\n%s'%OnlinetestPassword
	data = data.encode()
	print(data)
	with open('.\\OnlinetestPassword.txt', 'wb') as f:
		f.write(data)



if __name__ == '__main__':
	url1 = 'http://172.16.4.223:12001/apis/back/oldSystem/PassGet'
	url = 'http://172.16.4.223:12001/privilege/front/users/login'
	get_OnlinetestPassword(url1)

