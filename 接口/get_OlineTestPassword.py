#coding=utf-8
from email.mime.text import MIMEText
import requests,json,time,smtplib,re

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
	# data = data.encode()
	print(data)
	# with open('.\\OnlinetestPassword.txt', 'wb') as f:
	# 	f.write(data)
	return data


#发送邮件函数
def Email(rs_time):
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    content = response_time+rs_time
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="wcmynglgfomygecd" # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers =['高亚静<838456406@qq.com>','lin@leyoujia.com<lin@leyoujia.com>','袁猛<yuanm@leyoujia.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'线上测试密码'  #主题
    message['Subject'] = subject

    try:
        c = smtplib.SMTP()
        c.connect(mail_host, 25) # 25 为 SMTP 端口号
        c.login(mail_user,mail_pass)  #登录
        c.sendmail(mail_user,receivers,message.as_string())    #发送
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)
        print ("Error: 无法发送邮件")





 # ##############################################
        # 从dubbo后台获取直连ip

def dubboGetip(interface, huanjing, tanchuangbz):

	'''
	# 从dobbo中心获取服务的直连ip。
	:param interface: 服务名称
	:param huanjing: 调用环境
	:param tanchuangbz: 当获取不到ip时是否弹窗确认打开dubbo后台管理中心
	:return:
	'''
	# 弹窗确认结果，默认为False
	ry = False
	if u'正式' in huanjing or u'生产' in huanjing:
		huanjing = '172.16.4.223:8084'
	elif u'3.100' in huanjing or u'线下测试' in huanjing:
		huanjing = '172.16.4.114:9080'
	elif u'22.100' in huanjing or u'容器' in huanjing:
		huanjing = '172.16.22.100:9080'
	elif u'2.54' in huanjing or u'线上测试' in huanjing:
		huanjing = '192.168.3.70:9080'
	else:
		print(u'环境指定错误，默认使用3.100')
		huanjing = '172.16.4.114:9080'
	try:
		headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate",
				   "Connection": "keep-alive",
				   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
				   "Host": "172.16.4.223:8084",
				   "Cookie": "_ga=GA1.1.1890888338.1580476038; HISTORY=\"com.jjshome.im.service.dubbo.NimAccidService..../governance/services/com.jjshome.im.service.dubbo.NimAccidService/providers\\.\\.\\.\\.\\.\\.com.jjshome.im.service.dubbo.INimRoomService..../governance/services/com.jjshome.im.service.dubbo.INimRoomService/providers\"",
				   "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
				   "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}
		url = 'http://%s/governance/services/%s/providers' % (huanjing, interface)
		url_t = 'http://%s/governance/services?keyword=%s' % (huanjing, interface)
		# 发送请求，查询dubbo后台，获取ip和端口
		try:
			r = requests.get(url=url, headers=headers, timeout=5)
			r = re.findall('\d+\.\d+\.\d+\.\d+\:\d+', r.text)
		except:
			if tanchuangbz:
				print("请求失败")
		# 如果获取ip和端口成功
		if r:
			print(r)
			print(re.split(':', r[0]))
			# 如果是容器则特殊处理
			if u'22.100' in huanjing or u'容器' in huanjing:
				return ('172.16.22.100', '2008')
			return re.split(':', r[0])

	except:
		print("获取不到IP和端口")


#发送乐聊通知提醒
def IMsendinfo(ids, text, info,group='im-serve-attend',url=''):


	idsstr = ''
	# 如果是字符串则转为list
	if type(ids) != type([]):
		ids = ids.replace(';', ',')
		ids = ids.replace(u'，', ',')
		ids = re.split(',', ids)
	if ids:
		for i in ids:
			idsstr = u'%s"%s",' % (idsstr, i)
		idsstr = idsstr[:-1]
		print('idsstr:',idsstr)
	else:
		return

	msg = text.replace('\r\n', '')
	msg = msg.replace('\n', '')
	interface = 'com.jjshome.im.service.dubbo.NimAccidService'
	method = 'sendCustomMsg'
	# host = '192.168.196.6'    不知道什么原因这个IP会变，故不能写死
	# port = '26889'

	param = u'{"fromAccid":"servenumber000011","group":"%s","toAccids":[%s],"body":"{\\"type\\":8,\\"data\\":{\\"title\\":\\"%s\\",\\"content\\":\\"%s\\",\\"source\\":\\"im-serve-attend\\",\\"sourceName\\":\\"%s的温馨提示\\",\\"sourceType\\":\\"im-serve-fwsq\\",\\"url\\":\\"%s\\",\\"isOuterOpen\\":true}}"}' % (
		group, idsstr, info, msg, info, url)

	host, port = dubboGetip(interface=interface, huanjing=u'生产', tanchuangbz=False)

	try:
		url = u'http://172.16.100.12:29998/netdubbo'
		data = {'host': host, 'port': port, 'method': method, 'interface': interface, 'param': param, 'code': 'gbk',
				'outputbz': False}
		req = requests.post(url=url, data=data, timeout=5)
		print(req.text)
		print(u'调用远程服务成功。')
	except:
		print(u'乐聊通知处理出错！')



if __name__ == '__main__':
	url1 = 'http://172.16.4.223:12001/apis/back/oldSystem/PassGet'
	url = 'http://172.16.4.223:12001/privilege/front/users/login'
	rs_time = get_OnlinetestPassword(url1)
	ids = ["252613","388809"]
	text = rs_time
	info = 'onlinetest线上测试环境密码'
	IMsendinfo(ids, text, info,group='im-serve-attend',url='')
	# Email(rs_time)

