#coding=utf-8
import requests,json,time,sys,smtplib
from email.mime.text import MIMEText
from selenium import webdriver
reload(sys)
sys.setdefaultencoding( "utf-8" )

#获取登录cookie
url = "https://coa.leyoujia.com/aicp/mainremote"
token = '66920a879c283586dd6b4bf59e161820'
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