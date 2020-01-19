#coding=utf-8
import requests,json,time,sys,smtplib
from email.mime.text import MIMEText
from selenium import webdriver
reload(sys)
sys.setdefaultencoding( "utf-8" )

#获取登录cookie
url = "https://coa.leyoujia.com/aicp/mainremote"
token = '8846d63ee6b9af2c5476cced3b2f76d3'
payload = "msgBody=%7B%22time%22%3A%2203191419%22%2C%22workerId%22%3A%2206045224%22%2C%22ip%22%3A%22172.16.7.113%22%2C%22netId%22%3A%226C0B84A472DD%22%2C%22imei%22%3A%22pcMac-6C0B84A472DD%22%2C%22token%22%3A%22"+str(token)+"b3bde93c9%22%7D"
headers = {
    'appname': "pc-im",
    'deptname': "测试部",
    'deptnumber': "550146",
    'empname': "袁猛",
    'empno': "252613",
    'empnumber': "06045224",
    'imei': "pcMac-6C0B84A472DD",
    'methodcode': "50012",
    'servicecode': "40002",
    'v': "3",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "76b0a19f-9a6c-2816-1854-79a496017d54"
    }
headers['token']=token
response = requests.request("POST", url, data=payload, headers=headers)
a = json.loads(response.text)
print (a)
token = a['data']['secretKey']
print (token)


#发送邮件函数
def Email():
    content = u'网点地图all/map查询失败，请及时处理'
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="kzqownmlsecdgedd" # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers =['袁猛<1093040152@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'网点地图all/map查询失败，请及时处理'  #主题
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



#使用cookie登录并获取页面cookie
driver = webdriver.Chrome()
driver.get("https://i.leyoujia.com/jjslogin/forward?id=%s"%token)
time.sleep(1)
cookie = driver.get_cookies()
print (cookie)
JSESSIONID = cookie[0]['name']
JSESSIONID_value = cookie[0]['value']


jjshome_uuid = cookie[1]['name']
jjshome_uuid_value = cookie[1]['value']

jjshome_sid = cookie[2]['name']
jjshome_sid_value = cookie[2]['value']

SESSION = cookie[3]['name']
SESSION_value = cookie[3]['value']

print ('JSESSIONID:',JSESSIONID)
print ('JSESSIONID_value:',JSESSIONID_value)
print ('------------------------------')
print ('jjshome_uuid:',jjshome_uuid)
print ('jjshome_uuid_value:',jjshome_uuid_value)
print ('------------------------------')
print ('jjshome_sid:',jjshome_sid)
print ('jjshome_sid_value:',jjshome_sid_value)
print ('------------------------------')
print ('SESSION:',SESSION)
print ('SESSION_value:',SESSION_value)
print ('------------------------------')

driver.close()
driver.quit()


url = "https://coa.leyoujia.com/kp/map/allMap"

payload = "business=fh&type=2"
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "18",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "_smt_uid=5e1544d6.1e092283;JSESSIONID=%s"%JSESSIONID_value,
    'host': "coa.leyoujia.com",
    'origin': "https://coa.leyoujia.com",
    'pragma': "no-cache",
    'referer': "https://coa.leyoujia.com/kp/map/index",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"
    # 'postman-token': "3b2fe9c7-f168-a72d-9e5f-a32daa5fd2ce"
    }

response = requests.request("POST", url, data=payload, headers=headers)

a = json.loads(response.text)
# print (a)
token = a['infoStr']


print (token)

if token==u'操作成功！':
    # Email()
    pass
else:
    #发送邮件
    Email()




