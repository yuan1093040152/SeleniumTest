#coding=utf-8
from selenium import webdriver
import time,requests,json,datetime

url = "https://coa.leyoujia.com/aicp/mainremote"

payload = "msgBody=%7B%22imei%22%3A%22pcMac-6C0B84A472DD%22%2C%22mac%22%3A%226C0B84A472DD%2C005056C00001%2C005056C00008%2C3035323042363737313642304135434620202020%2C204153594EFF%2C%22%2C%22lat%22%3A0%2C%22lng%22%3A0%2C%22ipStr%22%3A%22172.16.7.113%22%2C%22loginAddr%22%3A%22%22%2C%22username%22%3A%22r3Ie16252D9o%22%2C%22password%22%3A%228f2c264349d499d22be944ed736bc931%22%2C%22empNo%22%3A%22252613%22%2C%22appVer%22%3A%222.1.4.9%22%2C%22env%22%3A%22online%22%7D"
headers = {
    'appname': "pc-im",
    'empno': "252613",
    'iemi': "pcMac-6C0B84A472DD",
    'methodcode': "login",
    'servicecode': "40002",
    'v': "3",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "35d8775d-f98a-175d-7128-28893a70e230"
    }
#verify = False  验证SSL证书
response = requests.request("POST",url,data=payload,headers=headers,verify = False).text

print(response)
a = json.loads(response)
token = a['data']['data']['token']
print (token)



appName:pc-im
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
deptName:%25E6%25B5%258B%25E8%25AF%2595%25E9%2583%25A8
deptNumber:5501462
empName:%25E8%25A2%2581%25E7%258C%259B
empNo:252613
empNumber:06045224
imei:pcMac-6C0B84A472DD
methodCode:50001
Origin:app://im.leyoujia.com
serviceCode:40002
token:e86e8f39b18701ffa98eff89c7ae0595



msgBody:{"groupName":"袁猛 (测试部)等人","workerNos":"252613,203228,330813","owner":"252613","workerId":"06045224","imei":"pcMac-6C0B84A472DD"}

https://coa.leyoujia.com/aicp/mainremote




import requests

url = "https://coa.leyoujia.com/aicp/mainremote"

payload = "serviceCode=40002&methodCode=50001&msgBody=%7B%22groupName%22%3A%22%E8%A2%81%E7%8C%9B%20(%E6%B5%8B%E8%AF%95%E9%83%A8)%E7%AD%89666%22%2C%22workerNos%22%3A%22252613%2C203228%22%2C%22owner%22%3A%22252613%22%2C%22workerId%22%3A%2206045224%22%2C%22imei%22%3A%22pcMac-6C0B84A472DD%22%7D"
headers = {
    'appname': "pc-im",
    'deptname': "%25E6%25B5%258B%25E8%25AF%2595%25E9%2583%25A8",
    'deptnumber': "5501462",
    'empname': "%25E8%25A2%2581%25E7%258C%259B",
    'empno': "252613",
    'empnumber': "06045224",
    'imei': "pcMac-6C0B84A472DD",
    'methodcode': "50001",
    'origin': "app://im.leyoujia.com",
    'servicecode': "40002",
    'token': "04809ec3d94008a5d653e1b93d90e5ca",
    'v': "3",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "0df2a247-5633-dd9d-31d9-3cba40adaaf7"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)