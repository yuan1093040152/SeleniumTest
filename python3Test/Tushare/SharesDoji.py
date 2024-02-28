#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2024/2/27 19:51
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import smtplib

import  MySQLdb,time,datetime
from chinese_calendar import is_workday
from email.mime.text import MIMEText
from email.header import Header


class sharesdoji:

    def dateList(self):
        # 当前日期
        date = datetime.datetime.now().date()
        datelist = []


    #sql 查询
    def mysql(self,sql):
        db = MySQLdb.connect(host='localhost', user='root', passwd='admintest', port=3306, db='shares',
                             charset='utf8')  # 打开数据库连接
        cur = db.cursor()  # 使用cursor()方法获取操作游标
        cur.execute(sql)  # 使用execute方法执行SQL语句
        db.commit()  # 提交请求
        info = cur.fetchall()   #获取数据
        cur.close()   # 关闭游标
        db.close()  # 关闭连接
        return info


    #获取sql查询的数据
    def sharesUp(self):
        # nowdate = self.dateList()[0]
        # sql = "SELECT a.`NAME` FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE	market IN ('主板', '中小板') AND b.trade_date BETWEEN '%s' AND '%s' ;"%(nowdate,nowdate)
        sql = "SELECT a.`NAME`,b.`OPEN`,b.`CLOSE`,b.high,b.low  FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE	market IN ('主板', '中小板') AND b.trade_date BETWEEN '2024-02-27' AND '2024-02-27' ;"

        sharesup = self.mysql(sql)
        return sharesup


    #对sql 查询的数据清理
    def datahandle(self):
        uplist = []
        data = self.sharesUp()
        print(data)
        # for x in data:
        #     for y in x:
        #         uplist.append(y)
        # print (uplist)
        # return uplist




a = 15
b = 10
diff = abs(a - b)
print(diff)
# sharesdoji().datahandle()