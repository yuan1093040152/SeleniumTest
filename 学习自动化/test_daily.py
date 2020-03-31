#coding=utf-8
import requests,json,MySQLdb,time

def mysql(sql):
    db = MySQLdb.connect(host='172.16.3.10',user='zhaory',passwd='jjs2019',port=3306,db='zentao',charset='utf8')  #打开数据库连接
    cur = db.cursor()           #使用cursor()方法获取操作游标 
    cur.execute(sql)            #使用execute方法执行SQL语句
    db.commit()                 #提交请求
    values = cur.fetchall()     #使用 fetchone() 方法获取一条数据
    cur.close()                 #关闭数据库连接
    return values               #返回
    # value = mysql(sql)
	# print (value)
    # new=json.dumps(value,ensure_ascii=False)    #Unicode编码转换成中文
	# # print (new)
 #    number = (value[0][0])
 #    print (number)





if __name__ == '__main__':
	# name = u'资产系统V1.4.7机构三期'
	# start_time = '2019-12-05 00:00:00'
	# end_time = '2020-1-2 23:59:59'
	sql = "SELECT id FROM zentao.zt_module WHERE `name`='资产系统V1.4.9_优化需求' AND type = 'case';"
	number = mysql(sql)
	id = (number[0][0])
	print (id)



	sql1 = "SELECT u.realname ,(SELECT m.`NAME` FROM zt_module WHERE id=c.module),count(t.caseResult),sum(CASE t.caseResult WHEN 'pass' THEN 1 ELSE 0 END ),sum(CASE t.caseResult WHEN 'fail' THEN 1 ELSE 0 END ), sum( CASE t.caseResult WHEN 'blocked' THEN 1 ELSE 0 END ) FROM zt_case c LEFT JOIN zt_module m ON c.module = m.id LEFT JOIN zt_testresult t ON t.`case` = c.id LEFT JOIN zt_user u ON u.account = t.lastRunner WHERE t.date > '2019-12-05 00:00:00' and t.date < '2020-1-2 23:59:59' AND c.module in (SELECT id from zentao.zt_module WHERE path like CONCAT(',',12034,',%')) GROUP BY m.`NAME`,t.lastRunner;"
	number1 = mysql(sql1)
	for x in number1:
		for i in x:
			# pass
		# pass
			print (i)
		time.sleep(1)



