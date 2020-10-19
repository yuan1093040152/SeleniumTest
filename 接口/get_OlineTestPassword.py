#coding=utf-8
from email.mime.text import MIMEText
import requests,json,time,smtplib

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



if __name__ == '__main__':
	url1 = 'http://172.16.4.223:12001/apis/back/oldSystem/PassGet'
	url = 'http://172.16.4.223:12001/privilege/front/users/login'
	rs_time = get_OnlinetestPassword(url1)
	Email(rs_time)

