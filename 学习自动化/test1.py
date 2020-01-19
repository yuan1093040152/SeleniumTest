#coding=utf-8
import requests,json,MySQLdb

def mysql(sql):
    db = MySQLdb.connect(host='172.16.4.31',user='root',passwd='passwd4_31',port=33097,db='hr',charset='utf8')  #打开数据库连接
    cur = db.cursor()           #使用cursor()方法获取操作游标 
    cur.execute(sql)            #使用execute方法执行SQL语句
    db.commit()                 #提交请求
    values = cur.fetchall()     #使用 fetchone() 方法获取一条数据
    cur.close()                 #关闭数据库连接
    return values               #返回


sql = "SELECT emp_number,emp_name FROM hr.sys_emp WHERE emp_number = '01000098';"


value = mysql(sql)
print (value)
# new=json.dumps(value,ensure_ascii=False)    #Unicode编码转换成中文
# print (new)
emp_number = (value[0][0])
print (emp_number)


