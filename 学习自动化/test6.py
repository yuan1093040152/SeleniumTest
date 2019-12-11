#coding=utf-8
from selenium import webdriver
import time,re,json,MySQLdb
driver = webdriver.Chrome()
def login():
	url = 'http://172.16.3.100/jjslogin/tologin'
	driver.get(url)
	driver.maximize_window()
	driver.implicitly_wait(30)
	driver.find_element_by_xpath("//input[@id='workerStr']").send_keys(u'周棵')
	driver.find_element_by_xpath("/html/body/ul[@id='ui-id-1']/li[@class='ui-menu-item']/a[1]").click()
	driver.find_element_by_id("password").send_keys("123")
	driver.find_element_by_id("login_button").click()
	time.sleep(1)
	return driver
driver = login()
url2 = 'http://172.16.3.100/jjsxm/myProject/myProject-search'
data = 'pageNo=1&pageSize=20&workerId=01000098&cCode=-1&aCode=-1'
urldata = url2 + '?' + data
driver.get(urldata) 
source = driver.page_source
value = re.search('>{.+?}<',source).group()[1:-1]
print (value)
a = json.loads(value)
createId = a['data']['list'][0]['createId']
print (createId)
def mysql(sql):
    db = MySQLdb.connect(host='172.16.4.31',user='root',passwd='passwd4_31',port=33097,db='hr',charset='utf8')  #打开数据库连接
    cur = db.cursor()           #使用cursor()方法获取操作游标 
    cur.execute(sql)            #使用execute方法执行SQL语句
    db.commit()                 #提交请求
    values = cur.fetchall()     #使用 fetchone() 方法获取一条数据
    cur.close()                 #关闭数据库连接
    return values               #返回
sql = "SELECT emp_number,emp_name FROM hr.sys_emp WHERE emp_number = '01000098';"
value1 = mysql(sql)
print (value1)
new=json.dumps(value1,ensure_ascii=False)    #Unicode编码转换成中文
print (new)
emp_number = (value1[0][0])
print (emp_number)

if createId == emp_number: 	
 	print ("此接口数据正确")
else:
 	print ("接口数据错误")











# createId = dict['data']['list'][0]['createId']

# print (createId)



