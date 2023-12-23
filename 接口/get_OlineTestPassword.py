#coding=utf-8

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

	# print ('今日预发布环境登陆密码为：',OnlinetestPassword)
	data = OnlinetestPassword
	# data = data.encode()
	print(data)
	# with open('.\\OnlinetestPassword.txt', 'wb') as f:
	# 	f.write(data)

	# 创建md5对象并加密
	print("开始对线上密码：%s进行MD5加密......."%OnlinetestPassword)
	md5 = hashlib.md5()
	b = OnlinetestPassword.encode(encoding='utf-8')
	md5.update(b)
	pass_word = md5.hexdigest()
	print("MD5加密后为：%s"%pass_word)

	sql = "UPDATE sys_emp_pass SET pass_word = '%s';" %pass_word
	print(sql)
	db = MySQLdb.connect(host='172.16.3.233', user='root_uattest', passwd='PUSYPAB&&6_2**McGxWyDVm', port=34117, db='hr',charset='utf8')  # 打开数据库连接
	cur = db.cursor()  # 使用cursor()方法获取操作游标
	cur.execute(sql)  # 使用execute方法执行SQL语句
	db.commit()  # 提交请求
	# values = cur.fetchall()  # 使用 fetchone() 方法获取一条数据
	cur.close()  # 关闭数据库连接
	print("批量修改线上测试环境登录密码为：%s"%OnlinetestPassword)

	return data


#发送邮件函数
def Email(rs_time):
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    content = response_time+rs_time
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="pjosevrxdxurjeeg" # QQ邮箱登录的授权码
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
		huanjing = '172.16.3.233:8084'
	elif u'itest' in huanjing or u'ksitest' in huanjing:
		huanjing = '172.16.16.8:31426'
	else:
		print(u'环境指定错误，默认使用itest')
		huanjing = '172.16.16.8:31426'
	print('huanjing===', huanjing)
	try:
		headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate",
				   "Connection": "keep-alive",
				   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
				   "Host": huanjing,
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
		# 改成utf-8解决中文乱码 （������С�������Ǵ��ϰ࿨）
		data = {'host': host, 'port': port, 'method': method, 'interface': interface, 'param': param, 'code': 'utf-8',
				'outputbz': False}
		req = requests.post(url=url, data=data, timeout=5)
		print(req.text)
		print(u'调用远程服务成功。')
	except:
		print(u'乐聊通知处理出错！')



"""
1、利用消息平台发送UAT密码给相关人员
"""
def XXPT_fs(txt,title,emp_number,emp_name):
    url = "https://i.leyoujia.com/msg/im/addTemplateInfo"
    data ={
        "belongDept":"12",
        "laterRemind":"1",
        "pushMode": "1",
        "pushWorker": "2",
        "rank": "1",
        "title": title,
        "type": "1",
        "templateContents": [{"type":"text","value":txt}],

        "templateWorkers": [
                            {"type": "1",
                             "workerType": "1",
                             "value": emp_number,
                             "name": emp_name}
                            ]
    }
    headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding":"gzip, deflate, br",
               "Accept-Language":"zh-CN,zh;q=0.9",
               "Cache-Control":"no-cache",
               "Connection":"keep-alive",
               "Content-Length":"464",
               "Content-Type":"application/json; charset=UTF-8",
               "Cookie":"prefs={}; fhListCookies=; jjshome_uuid=2d8db24a-d505-94df-befa-fce33a6057be; _ga=GA1.2.469380103.1688031287; /hsl/index/house-list_guidance=1; cookiesId=67fd28febc684aa2b689cff24c43107f; ysl-list=1; reserve-list=1; token=t.ORD0x1QdtR11YEgLgNn0; gr_user_id=3fab8280-a3be-4c3e-bb5d-e2517dd30cd9; connect.sid=s%3A85-aogZtViP5TpwyLIgr5Dfqhj9R0Zb1.%2FdFAOCuSJ4XDikYu6bzsKwowklPrcx62icgEKERUM3g; JSESSIONID-FANG=MWY3Y2IzMDUtNzI2MS00ZWRkLTliMTYtNmQxNGZhZDI3ZDA0; JSESSIONID=8C62D5150084F58A28CB4B8D6072A1D9; proLEYOUJIA=MDJlYzFhOTItMzIzMi00YWRiLWIwNmMtMDdkMzgzYmE3YWE0; login-mac=; jjshome_sid=c6a53232-74a1-7b26-9781-61bc63dd5f5f; login-workerid=33029115; fatLEYOUJIA=N2U5YTIwNTctOTAxNS00ZTYzLWIwYmItNDlmZDkxZDk5MmE2",
               "Host":"i.leyoujia.com",
               "Origin":"https://i.leyoujia.com",
               "Pragma":"no-cache",
               "Referer":"https://i.leyoujia.com/lyj-menu/syssetting/SYS_XXTP?submenu=sent",
               "Sec-Fetch-Dest":"empty",
               "Sec-Fetch-Mode":"cors",
               "Sec-Fetch-Site":"same-origin",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
               "X-Requested-With":"XMLHttpRequest"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    s1 = response.json()
    return s1


"""
ids:发送的人员   例：[{'06045224': '袁猛'}, {'00410622': '冉成浩'}]
title:发送的标题   
text:发送的内容
"""
def js(ids,text,title):
    for i in ids:
        emp_number = list(i.keys())[0]
        emp_name = list(i.values())[0]
        sendinfo = XXPT_fs(text,title,emp_number,emp_name)
        print(emp_number,emp_name)




if __name__ == '__main__':
	url1 = 'http://172.16.3.233:12001/apis/back/oldSystem/PassGet'
	url = 'http://172.16.3.233:12001/privilege/front/users/login'
	rs_time = get_OnlinetestPassword(url1)
	# ids = ["袁猛","曾亮","汪永喜","孙杰","苏薇","杨耿晖","李珍一","黄慧","曾佩","王曼莹","刘颖","冉成浩"]
	#ids = ["252613","454949","405984","268709","104667","407662","428606","045682","029246","190539","265727","410622"]
	# ids = ["252613"]
	ids = [{'06045224': '袁猛'}, {'00410622': '冉成浩'}, {'77807633': '黄慧'}, {'02081317': '王曼莹'}, {'06058331': '刘颖'}]
	print(ids)
	text = rs_time
	title = 'UAT验收环境登陆密码'
	js(ids,text,title)

	# IMsendinfo(ids, text, info,group='im-serve-attend',url='')
	# Email(rs_time)

