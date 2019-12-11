#coding=utf-8
import smtplib,time
from email.mime.text import MIMEText
from email.header import Header
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

def Email(content):
# 第三方 SMTP 服务
	mail_host="smtp.qq.com" #设置服务器
	mail_user="1093040152@qq.com" #用户名
	mail_pass="oxafwswibywigfij" # QQ邮箱登录的授权码
	receivers =['袁猛<yuanm@leyoujia.com>','吴磊<wul@leyoujia.com>','杨旭东<yangxd@leyoujia.com>','浮夸<1719422952@qq.com>']
	# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
	message = MIMEText(content, 'plain', 'utf-8') #文本内容
	message['From'] = mail_user # 发送者   （发送人同QQ备注，可不写）
	message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
	subject = u'测试发邮件,打扰了1'  #主题
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

def aaa(url,name):
	try:
		driver = webdriver.Chrome()
		driver.get(url)
		# driver.maximize_window()
		driver.implicitly_wait(30)
		driver.find_element_by_name("userName").send_keys(name)
		driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
		driver.find_element_by_id("password").send_keys("1")
		driver.find_element_by_id("login_button").click()
		time.sleep(3)
		exc = driver.find_element_by_xpath("//*[@id='topics']/div[1]/div/div/div[2]/span[2]/a").text
		print (u'登录人：'+exc)
		if exc == name:
			print (u'登录成功')
		time.sleep(1)
		driver.close()
		
	except:
		content = u'登录异常'
		Email(content)
		# print (content)

if __name__ == '__main__':
	url = 'http://172.16.3.100/jjslogin/index'
	name = u'吴磊'
	login = aaa(url,name)

