#coding=utf-8
import requests,sys,smtplib,io
from bs4 import BeautifulSoup
from email.mime.text import MIMEText

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def link_list(url):

    # try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    start_html = requests.get(url, headers=headers,timeout = 2000)
    demo = start_html.text
    # print(demo)
    soup = BeautifulSoup(demo, 'lxml')
    print(soup)

    # a = soup.select('div.wbpro-side-main.SideIndex_sideMain_3jrwf')
    # print(a)
    #     link_all = soup.find_all('a',class_='contentHerf')
    #     # print(link_all)
    #
    #     inurl = 'https://www.qiushibaike.com'
    #
    #     delete()
    #
    #
    #
    #     with open('E:\\test\\haha.txt', 'a',encoding='utf-8') as f:
    #
    #         for link in link_all:
    #             src = inurl+link['href']
    #             print(src)
    #
    #             start_html_1 = requests.get(src, headers=headers,timeout = 2000)
    #             demo = start_html_1.text
    #             soup1 = BeautifulSoup(demo, 'lxml')
    #             # print(soup1)
    #
    #             try:
    #                 title = soup1.find('div',class_="content").get_text()
    #                 print(title)
    #                 f.write('\n'+title + '\n')
    #             except:
    #                 pass
    #
    #             try:
    #                 shenping = soup1.find('div',class_="comment-title").get_text()
    #                 print(shenping)
    #                 f.write('\n' + shenping + '\n')
    #             except:
    #                 pass
    #
    #
    #             sp_list = soup1.select('div.comment-block.clearfix.floor-8')
    #             # print(sp_list)
    #
    #             for sp in sp_list:
    #                 sp_name = sp.find('a', class_="userlogin").get_text()
    #                 sp_info = sp.find('span', class_="body").get_text()
    #                 print(sp_name + ':' + sp_info)
    #                 f.write('\n' + sp_name + ':' + sp_info + '\n')
    #             f.write('\n' +'----------------------------------------------------')
    #
    # except:
    #     print('爬取失败')
    #     pass





# 清空文件内容
# def delete():
#     with open('E:\\test\\haha.txt', 'r+',encoding='UTF-8') as f:
#         read = f.read()
#         f.seek(0)
#         f.truncate()
#     f.close()
#
#
# #读取文件信息
# def txt_info():
#      with open('E:\\test\\haha.txt','r',encoding='UTF-8') as f:
#          txt_info1 = f.read()
#          # print (txt_info1)
#          return txt_info1



def Email():
    content = txt_info()
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="pjosevrxdxurjeeg" # QQ邮箱登录的授权码
    receivers =['袁猛<1093040152@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'每日一笑，愿你开心一整天'  #主题
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
    url = 'https://shenzhen.leyoujia.com/esf/'

    link_list(url)
    # Email()