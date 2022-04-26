#coding=utf-8

from borax.calendars.lunardate import LunarDate
from email.mime.text import MIMEText
import datetime,MySQLdb,json,re,smtplib,time

def get_time():
    #获取当前时间
    time1 = datetime.datetime.now()
    print(time1)
    print(time1.year,time1.month,time1.day)


    #获取当前日期的农历
    #create_time = "%4d-%02d-%02d%%" % (year, month, day)  # %02d 意思是填充至两位有效数字,不够以0补充,注意不能把0改为其他的以其他数字补充
    get_lunarCalendar = LunarDate.today()
    get_lunarCalendar = '%4d-%02d-%02d'%(get_lunarCalendar.year,get_lunarCalendar.month,get_lunarCalendar.day)
    print(get_lunarCalendar)


    #获取当前日期的公历
    # time2 = datetime.datetime.now()
    # print('-----',time2)
    # get_time= LunarDate(time2.year,time2.month,time2.day, 0)
    #
    # get_GregorianCalendar = get_time.to_solar_date()
    # print(get_GregorianCalendar)
    # print(get_GregorianCalendar.year,get_GregorianCalendar.month,get_GregorianCalendar.day)


    return get_lunarCalendar


def birthday_time():
    get_GregorianCalendar = get_time()
    print(get_GregorianCalendar)
    get_GregorianCalendar = str(get_GregorianCalendar)[4:]
    print(get_GregorianCalendar)
    sql = "SELECT a.emp_name FROM sys_emp a ,sys_dept b ,sys_emp_detail c WHERE a.dept_number = b. number AND b.comp_id IN ('330016','330007') AND a.emp_number = c.worker_id  AND a.login_status in (1,2,3) AND a.emp_status in (0,1,2,3,4) AND a.account_status in (0,1,2) AND c.birth_date LIKE'%%%s%%';"%(get_GregorianCalendar)
    #sql = "SELECT a.emp_name FROM sys_emp a ,sys_dept b ,sys_emp_detail c WHERE a.dept_number = b. number AND b.comp_id = '330016' AND a.emp_number = c.worker_id  AND a.login_status in (1,2,3) AND a.emp_status in (0,1,2,3) AND a.account_status in (0,1,2) AND c.birth_date LIKE'%-06-13%';"
    print(sql)

    # db = MySQLdb.connect(host='172.16.4.223',user='coa_group_qhn_sj',passwd='jjszrExXC1Bu4uH6jktL+_&^',port=35113,db='hr',charset='utf8')  #打开数据库连接
    db = MySQLdb.connect(host='172.16.22.101',user='root',passwd='admintest',port=33096,db='hr',charset='utf8')  #打开数据库连接

    cur = db.cursor()           #使用cursor()方法获取操作游标
    cur.execute(sql)            #使用execute方法执行SQL语句
    db.commit()                 #提交请求
    values = cur.fetchall()     #使用 fetchone() 方法获取一条数据
    cur.close()                 #关闭数据库连接

    return values               #返回

#发送邮件函数
def Email(str1):
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    content = response_time+u'今天生日成员名单：%s'%str1   #内容
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="lnacyybewdgngjcb" # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers =['袁猛<1093040152@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'今天有人过生日，记得送祝福'  #标题
    message['Subject'] = subject

    try:
        c = smtplib.SMTP()
        c.connect(mail_host, 25) # 25 为 SMTP 端口号
        c.login(mail_user,mail_pass)  #登录
        c.sendmail(mail_user,receivers,message.as_string())    #发送
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print (e)
        print ("Error: 无法发送邮件")


if __name__ == '__main__':
    values = birthday_time()
    print(type(values))

    d = ''.join(str(values))
    print(d)

    #去掉字符串内的符号（只留中文）
    str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\(\)\']", "", d)
    print(str)

    #替换
    str1 = [str.replace(" ", ",")]
    str2 = str1[0].strip()
    print(len(str2))


    if len(str2) == 0:
        print('今天没人过生日')
    else:
        Email(str2)












