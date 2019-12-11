#coding=utf-8
import requests,json,MySQLdb
url = 'http://172.16.3.100/jjsxm/myProject/myProject-search'
data ='pageNo: 1,pageSize: 20,workerId: 01000098,cCode: -1,aCode: -1'
headers = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Content-Length': '172',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 'guideValue=01000098; _smt_uid=5ae3c219.55b0e4a9; JSESSIONIDUE=333B2979F594B2E94719CA71CA382990; JSESSIONID=6F192EDB8C454D48BAE52EF0CA60D29C',
	'Host': '172.16.3.100',
	'Origin': 'http://172.16.3.100',
	'Referer': 'http://172.16.3.100/jjsxm/myProject',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}
res = requests.get(url,data = data,headers=headers)

print (res.text)

# a = json.loads(res.text)
# print type(a)
# createId = dict['data']['list'][0]['createId']
# print (createId)

# def mysql(sql):
#     db = MySQLdb.connect(host='172.16.4.31',user='root',passwd='passwd4_31',port=33097,db='hr',charset='utf8')  #打开数据库连接
#     cur = db.cursor()           #使用cursor()方法获取操作游标 
#     cur.execute(sql)            #使用execute方法执行SQL语句
#     db.commit()                 #提交请求
#     values = cur.fetchall()     #使用 fetchone() 方法获取一条数据
#     cur.close()                 #关闭数据库连接
#     return values               #返回
# sql = "SELECT emp_number,emp_name FROM hr.sys_emp WHERE emp_number = '01000098';"
# value = mysql(sql)
# print (value)
# new=json.dumps(value,ensure_ascii=False)    #Unicode编码转换成中文
# print (new)
# emp_number = (value[0][0])
# print (emp_number)

# if createId == emp_number: 	
#  	print ("此接口数据正确")
# else:
#  	print ("接口数据错误")
 