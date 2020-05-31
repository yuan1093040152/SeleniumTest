#coding=utf-8
from selenium import webdriver
import time,requests,json,datetime
import sys,importlib

importlib.reload(sys)
# reload(sys)
# sys.setdefaultencoding('utf8')

url = "https://coa.leyoujia.com/aicp/mainremote"
#测试营销副总裁
# username = 'h4p493780rKv'
# password = '03d25b3dc4f4a37fc9ceb5baa455d594'
# emp_no = '087394'
username = '袁猛'
username = username.encode('utf-8')
password = 'mm711232'
emp_no = '252613'

data = "msgBody=%7B%22imei%22%3A%22pcMac-6C0B84A472DD%22%2C%22mac%22%3A%226C0B84A472DD%2C005056C00001%2C005056C00008%2C3035323042363737313642304135434620202020%2C204153594EFF%2C%22%2C%22" \
       "lat%22%3A0%2C%22lng%22%3A0%2C%22ipStr%22%3A%22172.16.5.15%22%2C%22loginAddr%22%3A%22%22%2C%22username%22%3A%22"+str(username)+"%22%2C%22password%22%3A%22"\
       +str(password)+"%22%2C%22empNo%22%3A%22"+str(emp_no)+"%22%2C%22appVer%22%3A%222.1.5.0%22%2C%22sysVer%22%3A%226.1.7601%22%2C%22env%22%3A%22online%22%7D"
headers = {
    'appname': "pc-im",
    'iemi': "pcMac-6C0B84A472DD",
    'methodcode': "login",
    'servicecode': "40002",
    'v': "3",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "3511a564-1c12-2dc6-0a53-66fb5f2e3b89"
}
headers['empno'] = emp_no
time.sleep(2)
#verify = False  验证SSL证书
# response = (requests.request("POST",url,data=data,headers=headers,verify = False)).text   #如果报SSL错误，加这个条件
response = (requests.request("POST",url,data=data,headers=headers)).text
# print(response)
a = json.loads(response)
print (a)
token = a['data']['data']['token']
workerId = a['data']['data']['workerId']
nowtime = datetime.datetime.now().strftime('%m%d%H%M')
deptnumber = a['data']['data']['deptNumber']
deptname = a['data']['data']['deptName']
name = a['data']['data']['name']
empno = a['data']['data']['workerNo']
empnumber = a['data']['data']['workerId']
print (token)

data1 = "msgBody=%7B%22time%22%3A%22"+str(nowtime)+"%22%2C%22workerId%22%3A%22"\
        +str(workerId)+"%22%2C%22ip%22%3A%22172.16.7.113%22%2C%22netId%22%3A%226C0B84A472DD%22%2C%22imei%22%3A%22pcMac-6C0B84A472DD%22%2C%22token%22%3A%22"+str(token)+"%22%7D"
print ('data1=',data1)
headers1 = {
'appname': "pc-im",
'imei': "pcMac-6C0B84A472DD",
'methodcode': "50012",
'servicecode': "40002",
'v': "3",
'content-type': "application/x-www-form-urlencoded",
'cache-control': "no-cache",
'postman-token': "76b0a19f-9a6c-2816-1854-79a496017d54"
}
headers1['token'] = token
headers1['empnumber'] = empnumber
headers1['empno'] = empno
headers1['deptnumber'] = deptnumber
headers1['deptname'] = deptname
headers1['empname'] = name

print (headers1)
time.sleep(1)
# response1 = requests.request("POST",url,data=data1, headers=headers1,verify = False).text    #如果报SSL错误，加这个条件
response1 = requests.request("POST",url,data=data1, headers=headers1).text
print(response1)
b = json.loads(response1)
id = b['data']['secretKey']
print (id)
time.sleep(1)
url = 'https://i.leyoujia.com/jjslogin/forward?id='+id
print (url)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)
# driver.close()
