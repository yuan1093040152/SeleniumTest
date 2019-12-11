#coding=utf-8
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import smtplib,time
from email.mime.text import MIMEText

class login(unittest.TestCase):
    def setUp(self):               #开始执行前需要做的事（每条用例都会执行）
        print (u'开始执行')
        self.driver = webdriver.Chrome()
        self.driver.get('http://172.16.3.100/jjslogin/index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):          #执行用例结束后需要做的事情（每条用例都会执行）
        print (u'已执行完')
        self.driver.close()

    def test_haha(self):       #用例1
        self.driver.find_element_by_name("userName").send_keys( u'吴磊')
        self.driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
        self.driver.find_element_by_id("password").send_keys("1")
        self.driver.find_element_by_id("login_button").click()
        time.sleep(3)
        exc = self.driver.find_element_by_xpath("//*[@id='topics']/div[1]/div/div/div[2]/span[2]/a").text
        print (u'登录人：' + exc)
        if exc == u'吴磊':
            print (u'登录成功')
        time.sleep(1)

    def test_huhu(self):  # 用例2
        self.driver.find_element_by_name("userName").send_keys(u'袁猛')
        self.driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
        self.driver.find_element_by_id("password").send_keys("1")
        self.driver.find_element_by_id("login_button").click()
        time.sleep(3)
        exc = self.driver.find_element_by_xpath("//*[@id='topics']/div[1]/div/div/div[2]/span[2]/a").text
        print (u'登录人：' + exc)
        if exc == u'袁猛':
            print (u'登录成功')
        time.sleep(1)

def Email(content):
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="oxafwswibywigfij" # QQ邮箱登录的授权码
    receivers =['袁猛<yuanm@leyoujia.com>','吴磊<wul@leyoujia.com>','杨旭东<yangxd@leyoujia.com>','浮夸<1719422952@qq.com>']

    #带附件
    message = MIMEMultipart()
    file_path = 'C:\\Users\\admin\\Desktop\\res.html'
    sendfile = open(file_path, "r").read()  # 读取测试报告路径
    # 如下几行是为了以附件的形式，发送邮件
    msg = MIMEText(sendfile, "base64", "utf-8")
    msg["Content-Type"] = "application/octet-stream"
    msg["content-Disposition"] = "attachment;filename=TestReport.html"
    message.attach(msg)

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message.attach(MIMEText(content, 'plain', 'utf-8')) #文本内容
    message['From'] = mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'测试发邮件,打扰了'  #主题
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

if __name__ == '__main__':    #直接执行该文件
    # unittest.main()
    test_suite = unittest.TestSuite()      # 创建一个测试集合
    test_suite.addTest(unittest.makeSuite(login))     #使用makeSuite方法添加所有的测试方法
    path =  'C:\\Users\\admin\\Desktop\\res.html'   # 打开一个保存结果的html文件
    with open(path, 'wb+') as f:
        runner = HTMLTestRunner(stream=f,title=u'测试报告',description=u'下面是测试用例执行情况，请领导查阅')     # 生成执行用例的对象
        runner.run(test_suite)        # 执行测试套件
        time.sleep(1)
        time.sleep(1)
    f.close()
    content = u'附件为最新的测试报告，请查阅：'
    Email(content)


