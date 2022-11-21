#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/7/7 22:31
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


class sharesselect:


    def dateList(self):
        # 当前日期
        date = datetime.datetime.now().date()
        datelist = []

        # 打印最近一周工作日
        for i in range(7):
            if is_workday(date):
                datelist.append(date)
            else:
                pass
            date = date + datetime.timedelta(-1)
        return datelist


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
        nowdate = self.dateList()[0]
        sql = "SELECT a.`NAME` FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE	market IN ('主板', '中小板') AND b.trade_date BETWEEN '%s' AND '%s' and b.pct_chg < -2 AND b.`CLOSE` > b.`OPEN`;"%(nowdate,nowdate)
        sql2 = "SELECT a.`NAME` FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE	market IN ('主板', '中小板') AND b.trade_date BETWEEN '2022-07-07' AND '2022-07-07' and b.pct_chg < -2 AND b.`CLOSE` > b.`OPEN`;"

        sharesup = self.mysql(sql)
        return sharesup


    #对sql 查询的数据清理
    def datahandle(self):
        uplist = []
        data = self.sharesUp()
        for x in data:
            for y in x:
                uplist.append(y)
        print (uplist)
        return uplist


    #查询两天内收盘价大于开盘价
    def sharesrise(self):
        nowdate1 = self.dateList()[0]
        nowdate2 = self.dateList()[1]
        uplist = self.datahandle()
        up = []
        for i in uplist:
            sql3 = "SELECT b. `OPEN`,b. `CLOSE` FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE a.`NAME` = '%s' AND b.trade_date BETWEEN '%s' AND '%s';"%(i,nowdate2,nowdate1)
            print(sql3)
            close = self.mysql(sql3)
            print(close)
            listx = close[0]
            listy = close[1]
            print(listx)
            print(listy)
            if listx[0] <listx[1] and listy[0] <listy[1]:
                up.append(i)
            else:
                pass
        print(up)
        return up



    # 发送邮件
    def Email(self):
        upstoplist = self.sharesrise()
        title = '20CM涨停的股'
        content = '明天看涨的股票：%s'%upstoplist
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "1093040152@qq.com"  # 用户名
        mail_pass = "bjqjikmijcobfece"  # QQ邮箱登录的授权码
        # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>']
        receivers = ['袁猛<1093040152@qq.com>']
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(content, 'plain', 'utf-8')  # 文本内容
        message['From'] = '袁猛<1093040152@qq.com>'  # mail_user # 发送者   （发送人同QQ备注，可不写）
        message['To'] = ','.join(receivers)  # 这里必须要把多个邮箱按照逗号拼接为字符串
        subject = title  # 主题
        message['Subject'] = subject

        try:
            c = smtplib.SMTP()
            c.connect(mail_host, 25)  # 25 为 SMTP 端口号
            c.login(mail_user, mail_pass)  # 登录
            c.sendmail(mail_user, receivers, message.as_string())  # 发送
            print("邮件发送成功！")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")



sharesselect().Email()