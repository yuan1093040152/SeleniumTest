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