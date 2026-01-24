# coding=utf-8
"""
@Author  : Yuan Meng
@File    : get_OlineTestPassword.py
@Time    : 2026/1/24 10:56
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from email.mime.text import MIMEText
import requests,json,time,smtplib,re,MySQLdb,hashlib



def get_sessionID(url):
	body = 'loginName=tandf&loginPass=123456'
	headers = {
	'Host':'172.16.3.233:12001',
	'Connection': 'keep-alive',
	'Content-Length': '32',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With': 'XMLHttpRequest',
	'sessionID': 'null',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Origin': 'http://172.16.3.233:12001',
	'Referer': 'http://172.16.3.233:12001/',
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
	'Host': '172.16.3.233:12001',
	'Connection': 'keep-alive',
	'Content-Length': '0',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With':'XMLHttpRequest',
	'sessionID':sessionID ,
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
	'Origin': 'http://172.16.3.233:12001',
	'Referer': 'http://172.16.3.233:12001/portal/index',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': '_ga=GA1.1.1238046553.1594955626'
	}
	response = requests.request("POST", url1,headers=headers)
	print (response.text)
	text = response.text
	load = json.loads(text)
	OnlinetestPassword = load['msg']

	print ('今日预发布环境登陆密码为：',OnlinetestPassword)
	data = OnlinetestPassword
	# data = data.encode()
	# print(data)
	# with open('.\\OnlinetestPassword.txt', 'wb') as f:
	# 	f.write(data)

	# 创建md5对象并加密
	# print("开始对线上密码：%s进行MD5加密......."%OnlinetestPassword)
	# md5 = hashlib.md5()
	# b = OnlinetestPassword.encode(encoding='utf-8')
	# md5.update(b)
	# pass_word = md5.hexdigest()
	# print("MD5加密后为：%s"%pass_word)
	#
	# sql = "UPDATE sys_emp_pass SET pass_word = '%s';" %pass_word
	# print(sql)
	# db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117, db='hr',charset='utf8')  # 打开数据库连接
	# cur = db.cursor()  # 使用cursor()方法获取操作游标
	# cur.execute(sql)  # 使用execute方法执行SQL语句
	# db.commit()  # 提交请求
	# values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
	# cur.close()  # 关闭数据库连接
	# print("批量修改线上测试环境登录密码为：%s"%OnlinetestPassword)
	#
	# return data


if __name__ == '__main__':
	url1 = 'http://172.16.3.233:12001/apis/back/oldSystem/PassGet'
	url = 'http://172.16.3.233:12001/privilege/front/users/login'
	rs_time = get_OnlinetestPassword(url1)
	# ids = ["袁猛","曾亮","汪永喜","孙杰","苏薇","杨耿晖","李珍一","黄慧","曾佩","王曼莹","刘颖","冉成浩"]
	#ids = ["252613","454949","405984","268709","104667","407662","428606","045682","029246","190539","265727","410622"]
	# ids = ["252613"]
	# ids = [{'06045224': '袁猛'}, {'00410622': '冉成浩'},  {'02081317': '王曼莹'}, {'06058331': '刘颖'}]
	# ids = [{'06045224': '袁猛'}]
	# print(ids)
	# text = rs_time
	# title = 'UAT验收环境登陆密码'
	# Cookie = 'jjshome_uuid=891fccac-b5eb-1f92-4e22-5939da7824c3; prefs={}; gr_user_id=06281673-fdf3-4867-903f-bcf9a6ccc70e; cookiesId=e5ee328c2dbf446e8a58f673a6176bc1; agentCardhd_time=1; fhListCookies=; /hsl/index/house-list_guidance=1; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1710320509; Hm_lvt_728857c2e6b321292b2eb422213d1609=1710320509; token=t.gIN6vT27o5V0xhHA41iW; JSESSIONID=21D88BD23B4443BA399643AEF0209705; fatLEYOUJIA=YzBjMmIxY2YtZDkzOC00NGRmLTk2NjgtZjkzYzhiOGFlMTUz; login-workerid=06045224; lyj_pc_token=XCE7TuPxFgcWmcocMiGlSTNErDNpB4jt; proLEYOUJIA=M2Q2ZWM4ZDEtZjEzNC00ODhjLTk0MjItZDcwMDUxZWQ1Y2Ri; login-mac=dc02f04c52b58e4751f9223b9d2fe776; jjshome_sid=48d2682f-98fc-6918-c2e8-fe96f6fb5ce2'
	# js(ids,text,title)

	# IMsendinfo(ids, text, info,group='im-serve-attend',url='')
	# Email(rs_time)