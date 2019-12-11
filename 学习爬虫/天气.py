#coding=utf-8
import requests,sys,smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
reload(sys)
sys.setdefaultencoding( "utf-8" )



def city_url(url):
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    start_html = requests.get(url,headers=headers)
    demo = start_html.text
    # print (demo)
    soup = BeautifulSoup(demo,'lxml')
    return soup
    # print soup

def tianqi():

    delete()

    with open('E:\\test\\weather.txt', 'a') as f:


        soup = city_url(url)

        for i in range(1, 2):
            # 查询日期和星期
            # test01 = (soup.find('div', class_="day7").find('ul', class_="week").find_all('li'))[i]
            # test011 = test01.get_text()
            # print u'日期:  %s' % test011
            # f.write(u'日期:  %s' % test011 + '\n')

            # 查询天气  soup.select_one('ul.txt.txt2')  查询有多个class值的标签
            test02 = (soup.find('div', class_="day7").select_one('ul.txt.txt2').find_all('li'))[i]
            test022 = test02.get_text()
            # print u'天气：  %s' % test022

            # f.write(u'天气：  %s' % test022 + '\n')

            # 查询温度
            test03 = (soup.find('div', class_="day7").find('div', class_="zxt_shuju").find_all('li'))[i]
            test04 = test03.get_text()
            # 最高
            test05 = test04[:2]
            # print u'最高温度:  %s℃' % test05
            # f.write(u'最高温度:  %s℃' % test05 + '\n')

            # 最低
            test06 = test04[2:]
            # print u'最低温度:  %s℃' % test06
            # f.write(u'最低温度:  %s℃' % test06 + '\n')

            # 风向
            test07 = (soup.find_all('ul', class_="txt"))[1]
            test08 = (test07.find_all('li'))[i].get_text()
            # print u'风向:  %s' % test08
            # f.write(u'风向:  %s' % test08 + '\n')
            # f.write('----------------------------------------' + '\n')
            if test022 == u'晴':
                print u'明天天气:%s，请注意防晒哟~' % test022
                f.write('\n'+u'明天天气:%s，目之所及，皆是回忆~' % test022 + '\n')
            elif test022 == u'雨':
                print u'明天天气:%s，记得带伞哈~' % test022
                f.write('\n'+u'明天天气:%s，记得带伞哈~' % test022 + '\n')
            else:
                print u'明天天气:%s，这个天气变化多端，注意天气变化~' % test022
                f.write('\n'+u'明天天气:%s，这个天气变化多端，听天由命咯~' % test022 + '\n')

            if int(test05) - int(test06) >= 10:
                print u'明天温差较大，冷热交替，小心感冒流鼻涕，哈哈~'
                f.write(u'明天温差较大，冷热交替，小心感冒流鼻涕，哈哈~'+'\n')
            else:
                print u'明天温差不大，适合晒太阳，记得出来走走，赶走霉运~'
                f.write(u'明天温差不大，适合晒太阳，记得出来走走，赶走霉运~' + '\n')

            if int(test06) >= 18:
                print u'明天夜晚最低温度:%s℃，可根据实际情况决定被子的厚度~' % test06
                f.write(u'明天夜晚最低温度:%s℃，可根据实际情况决定被子的厚度~' % test06 + '\n\n\n')
            else:
                print u'明天夜晚最低温度:%s℃，请盖好被子，盖好小jiojio，可别感冒了哟~' % test06
                f.write(u'明天夜晚最低温度:%s℃，请盖好被子，盖好小jiojio，我要开始讲故事了~' % test06 + '\n\n\n')

        f.write(u'亲，以下是未来一周的天气，请查收 ~' + '\n\n')
        for i in range(7):
            # 查询日期和星期
            test01 = (soup.find('div',class_="day7").find('ul',class_="week").find_all('li'))[i]
            test011 = test01.get_text()
            print u'日期:  %s'%test011
            f.write(u'日期:  %s'%test011+'\n')


            #查询天气  soup.select_one('ul.txt.txt2')  查询有多个class值的标签
            test02 = (soup.find('div',class_="day7").select_one('ul.txt.txt2').find_all('li'))[i]
            test022 = test02.get_text()
            print u'天气：  %s'%test022
            f.write(u'天气：  %s'%test022+'\n')



            #查询温度
            test03 = (soup.find('div',class_="day7").find('div',class_="zxt_shuju").find_all('li'))[i]
            test04 = test03.get_text()
            #最高
            test05 = test04[:2]
            print u'最高温度:  %s℃'%test05
            f.write(u'最高温度:  %s℃'%test05+'\n')

            #最低
            test06 = test04[2:]
            print u'最低温度:  %s℃' % test06
            f.write(u'最低温度:  %s℃' % test06+'\n')


            #风向
            test07 = (soup.find_all('ul',class_="txt"))[1]
            test08 = (test07.find_all('li'))[i].get_text()
            print u'风向:  %s' %test08
            f.write(u'风向:  %s' %test08+'\n')
            f.write('----------------------------------------'+'\n')
        f.close()




# 清空文件内容
def delete():
    with open('E:\\test\\weather.txt', 'r+') as f:
        read = f.read()
        f.seek(0)
        f.truncate()
    f.close()


#读取文件信息
def txt_info():
     with open('E:\\test\\weather.txt','r') as f:
         txt_info1 = f.read()
         # print (txt_info1)
         return txt_info1



def Email():
    content = txt_info()
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="kzqownmlsecdgedd" # QQ邮箱登录的授权码
    receivers =['袁猛<1093040152@qq.com>','丽丽<1032158846@qq.com>','维维<283562659@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = u'妳在看天气，而我在看妳'  #主题
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
    city = 'shenzhen'
    url = 'https://www.tianqi.com/%s/' % city
    print url
    tianqi()
    Email()


