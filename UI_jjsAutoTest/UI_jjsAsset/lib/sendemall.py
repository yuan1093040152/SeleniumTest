#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/11/15 9:20
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from email.mime.text import MIMEText#专门发送正文
from email.mime.multipart import MIMEMultipart#发送多个部分
from email.mime.application import MIMEApplication#发送附件
import smtplib#发送邮件
import json
from UI_jjsAutoTest.UI_jjsAsset.config.readconfig import ReadConfig
# import sys,codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

"""UnicodeEncodeError: 'ascii' codec can't encode characters in position 11-12: ordinal not in range(128)"""

ReadConfig = ReadConfig()

class SendEmail:

    def __init__(self):
        self.addressee = ReadConfig.get_email('addressee') #收件人
        self.Sender = ReadConfig.get_email('send_user') #发件人
        self.password = ReadConfig.get_email('password') #密码
        self.subject = ReadConfig.get_email('subject') #主题
        self.email_text = ReadConfig.get_email('email_text') #正文
        self.server_address = ReadConfig.get_email('server_address') # 服务器地址




    def Email(self,file):
        # file =u'D:/output_report/output.xlsx'
        # file = self.parent_dir + '/output.xlsx'
        # parser = argparse.ArgumentParser()
        # parser.add_argument("email")
        # args = parser.parse_args()
        # param = vars(args)
        # email = param['email']
        # email = os.environ['email']

        emaillist = self.addressee
        print('邮箱为：', emaillist)
        #因配置文件读取过来的数据为str，需要转换成list
        a = emaillist.replace("\'", "\"")
        b = json.loads(a)

        for email in b:
            print(email)
            send_user = self.Sender  # 发件人
            password = self.password  # 授权码/密码
            receive_users = email  # 收件人，可为list
            subject = self.subject  # 邮件主题
            email_text = self.email_text  # 邮件正文
            server_address = self.server_address  # 服务器地址
            mail_type = '1'  # 邮件类型

            # 构造一个邮件体：正文 附件
            msg = MIMEMultipart()
            msg['Subject'] = subject  # 主题
            msg['From'] = send_user  # 发件人
            msg['To'] = receive_users  # 收件人

            # 构建正文
            part_text = MIMEText(email_text)
            msg.attach(part_text)  # 把正文加到邮件体里面去

            # 构建邮件附件
            # file = file           #获取文件路径
            part_attach1 = MIMEApplication(open(file, 'rb').read())  # 打开附件
            part_attach1.add_header('Content-Disposition', 'attachment', filename=self.subject+'.html')  # 为附件命名
            msg.attach(part_attach1)  # 添加附件

            # 发送邮件 SMTP
            smtp = smtplib.SMTP(server_address, 25)  # 连接服务器，SMTP_SSL是安全传输

            smtp.login(send_user, password)
            smtp.sendmail(send_user, receive_users, msg.as_string())  # 发送邮件
            print('邮件发送成功！')



if __name__ == '__main__':

    path = u'E:\\SeleniumTest\\UI_jjsAutoTest\\UI_jjsAsset\\report\\2021-11-15_10-50-59report.html'
    print(path)
    SendEmail().Email(file=path)