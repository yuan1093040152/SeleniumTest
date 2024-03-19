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

import  MySQLdb,time,datetime,json
from chinese_calendar import is_workday
from email.mime.text import MIMEText
from email.header import Header


class sharesdoji:

    def dateList(self):
        # 当前日期
        date = datetime.datetime.now().date()
        return date



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
        nowdate =  self.dateList()
        sql = "SELECT a.`NAME`,a.`symbol`,b.`OPEN`,b.`CLOSE`,b.high,b.low,b.pct_chg  FROM	shareslist a INNER JOIN sharesquotation b ON a.ts_code = b.ts_code WHERE	market IN ('主板', '中小板') AND b.trade_date BETWEEN '%s' AND '%s' ;"%(nowdate,nowdate)
        # sql = "SELECT b.`OPEN`,b.`CLOSE`,b.high,b.low  FROM	sharesquotation b  WHERE b.trade_date BETWEEN '2024-02-27' AND '2024-02-27' ;"
        print(sql)

        sharesup = self.mysql(sql)
        return sharesup


    #对sql 查询的数据清理
    def datahandle(self):
        uplist = []
        data1 = self.sharesUp()
        data = list(data1)
        for x in data:
            xx = list(x)
            NAME = xx[0]
            symbol = xx[1]
            OPEN = xx[2]
            CLOSE = xx[3]
            high = xx[4]
            low = xx[5]
            pct_chg = xx[6]

            if CLOSE < 5:
                pass

            elif CLOSE < 10 and abs(pct_chg)< 1 :
                if self.diff(OPEN, CLOSE) < 0.01:
                    if self.diff(high, low) < 0.1:
                        uplist.append(NAME)
                    else:
                        pass
                else:
                    pass

            elif CLOSE < 20 and abs(pct_chg)< 1 :
                if self.diff(OPEN,CLOSE) < 0.03:
                    if self.diff(high,low) < 0.2:
                        uplist.append(NAME)
                        # print('已添加',uplist)
                    else:
                        pass
                else:
                    pass

            elif CLOSE < 40 and abs(pct_chg)< 1 :
                if self.diff(OPEN,CLOSE) < 0.05:
                    if self.diff(high,low) < 0.3:
                        uplist.append(NAME)
                        # print('已添加',uplist)
                    else:
                        pass
                else:
                    pass

            elif CLOSE > 40 and abs(pct_chg)< 1  :
                if self.diff(OPEN,CLOSE) < 0.1:
                    if self.diff(high,low) < 0.4:
                        uplist.append(NAME)
                        # print('已添加',uplist)
                    else:
                        pass
                else:
                    pass

            else:
                pass


        print(uplist)
        return uplist




    def diff(self,a,b):
        return abs(a - b)

    # 发送邮件
    def Email(self, a):
        title = '十字星股票'
        content = '十字星股票：%s' % a

        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        smtp_port = 587
        mail_user = "1093040152@qq.com"  # 用户名
        mail_pass = "kjdwsramukzxfjda"  # QQ邮箱登录的授权码
        # receivers =['袁猛<1093040152@qq.com>','袁猛<1093040152@qq.com>','袁猛<1093040152@qq.com>']
        receivers = ['袁猛<1093040152@qq.com>']

        # 构造邮件内容
        subject = title  # 主题
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header(mail_user)
        message['To'] = Header(','.join(receivers))
        message['Subject'] = Header(subject)
        try:
            # 连接SMTP服务器
            smtp_obj = smtplib.SMTP(mail_host, smtp_port)
            smtp_obj.starttls()  # 使用TLS加密连接
            smtp_obj.login(mail_user, mail_pass)  # 登录发件人邮箱

            # 发送邮件
            smtp_obj.sendmail(mail_user, receivers, message.as_string())
            print("邮件发送成功")

        except Exception as e:
            print("邮件发送失败:", e)

        finally:
            smtp_obj.quit()



if __name__ == '__main__':

    a = sharesdoji().datahandle()
    sharesdoji().Email(a)