#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/5/26 8:44
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from selenium import webdriver
from email.mime.text import MIMEText
import requests,json,urllib3,time,smtplib
import urllib.parse
from threading import Lock, Thread
import requests
import sys
import traceback
from datetime import datetime

def login_im(empno,url):
    body = 'msgBody={"imei":"pcMac-6C0B84A472DD","mac":"6C0B84A472DD,3035323042363737313642304135434620202020,204153594EFF,","lat":0,"lng":0,"ipStr":"172.16.9.54","loginAddr":"","username":"g33l16252vb3","password":"8f2c264349d499d22be944ed736bc931","empNo":"252613","appVer":"2.3.6.6","sysVer":"6.1.7601","env":"online"}'
    headers = {
        'Host': 'coa.leyoujia.com',
        'Connection': 'keep-alive',
        'Content-Length': '453',
        'methodCode': 'login',
        'Sec-Fetch-Mode': 'cors',
        # 'Origin: chrome-extension':'//im.leyoujia.com',
        'serviceCode': 'login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'v':'3',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'empNo': empno,
        'appName': 'pc-im',
        'iemi': 'pcMac-6C0B84A472DD',
        'Sec-Fetch-Site': 'same-site',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=2F16682C3E34234AA071B02DEB46FB6A'
    }

    requests.packages.urllib3.disable_warnings() #移除SSL警告
    response = requests.request("POST", url, data=body, headers=headers,verify = False) #ssl验证:verify = False
    print (response.text)
    text = response.text
    load = json.loads(text)
    token = load['data']['data']['token']
    print(token)
    return token

def login_XXT(empno,url,empnumber):
    token = login_im(empno,url)
    body1 = 'msgBody={"time":"07242142","workerId":"77806702","ip":"172.16.9.54","netId":"6C0B84A472DD,3035323042363737313642304135434620202020,204153594EFF,","imei":"pcMac-6C0B84A472DD","token":"bc60c03505f3ad1871a4ec9e341d1eba"}'
    headers1 = {
        'Host': 'coa.leyoujia.com',
        'Connection': 'keep-alive',
        'Content-Length': '297',
        'methodCode': '50012',
        'Sec-Fetch-Mode': 'cors',
        'empNumber': empnumber,
        # 'Origin': 'chrome-extension://im.leyoujia.com',
        'deptName': '%25E6%25B5%258B%25E8%25AF%2595%25E8%2590%25A5%25E9%2594%2580%25E5%258C%25BA%25E5%259F%259F',
        'serviceCode': '40002',
        'empName': '%25E6%25B5%258B%25E8%25AF%2595%25E8%2590%25A5%25E9%2594%2580%25E5%2589%25AF%25E6%2580%25BB%25E8%25A3%2581',
        'v': '3',
        'empNo': empno,
        'deptNumber': '7472434',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'imei': 'pcMac-6C0B84A472DD',
        'appName': 'pc-im',
        'token': token,
        'Sec-Fetch-Site': 'same-site',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=2F16682C3E34234AA071B02DEB46FB6A'
    }

    response1 = requests.request('post',url,data=body1,headers=headers1,verify = False)
    print(response1.text)
    text1 = response1.text
    load1 = json.loads(text1)
    token1 = load1['data']['secretKey']
    print(token1)
    url_all="https://i.leyoujia.com/jjslogin/forward?id=%s"%token1
    print(url_all)
    return url_all

def CJ_list(empno,url,empnumber,name,url2,xm):
    url_all = login_XXT(empno,url,empnumber)

    # 使用cookie登录并获取页面cookie
    driver = webdriver.Chrome()
    driver.get(url_all)
    time.sleep(1)
    cookie = driver.get_cookies()
    print(cookie)

    for i in cookie:
        try:
            if 'jjshome_sid'==i['name']:
                jjshome_sid_value = i['value']
                print('jjshome_sid_value====',jjshome_sid_value)
        except:
            pass

    for i in cookie:
        try:
            if 'jjshome_uuid' == i['name']:
                jjshome_uuid_value = i['value']
                print('jjshome_uuid_value====', jjshome_uuid_value)
        except:
            pass

    for i in cookie:
        try:
            if '_smt_uid' == i['name']:
                _smt_uid_value = i['value']
                print('_smt_uid_value====', _smt_uid_value)
        except:
            pass

    for i in cookie:
        try:
            if 'JSESSIONID' == i['name']:
                JSESSIONID_value = i['value']
                print('JSESSIONID_value====', JSESSIONID_value)
        except:
            pass

    print('------------------------------')

    driver.close()
    driver.quit()

    #因JSESSIONID暂不知道什么原因，传入后取不了完整数据，所以写死
    JSESSIONID = 'B40590AB1500E2EA57C26EF758A6C672'
    cookie = 'jjshome_uuid=%s; _smt_uid=%s; /hsl/index/house-list_guidance=1; /hsl/house/house-detail_guidance=1; /community/communityDic/communityDic-list_guidance=1; /community/communityDic/communityDic-detail_guidance=1; /community/communityDg/communityDg-list_guidance=1; /community/communityDg/communityDg-dic_guidance=1; /community/communityDic/communityDic-add-view-batch_guidance=1; /community/communityDg/communityDg-add-batch-cache_guidance=1; /hsl/entrust/entrust-add_guidance=1; /hsl/index/own-house-list_guidance=1; cookiesId=bce302d180064c60bd921167c696573c; _ga=GA1.2.317993357.1611364094; agentCardhd_time=1; fhListCookies=; gr_user_id=75926756-dfea-419b-a884-306d3cc99060; iJSESSIONID=57F9684687F6B8DDAEEAC86F8098123E; testLEYOUJIA=ZWNmZGIzOWYtYzhhNi00MTEzLTk2NzgtNGE0ODJmMjA1MjZl; SESSION=OWE3MTAzMjAtYjk2Ny00ZDEwLWFmZjAtMWM2NjFjOTExYTU0; login-mac=6C-0B-84-A4-72-DD; SESSION=M2Q4OGExMGItZjMwNC00YzBiLTlhNzEtOTVjZWJmY2UzYmE4; _gid=GA1.2.1006926862.1622013004; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1621326471,1622013004,1622013731; Hm_lvt_728857c2e6b321292b2eb422213d1609=1622013004,1622013731; Hm_lpvt_728857c2e6b321292b2eb422213d1609=1622014000; Hm_lpvt_1851e6f08c8180e1e7b5e33fb40c4b08=1622014000; jjshome_sid=%s; default_city_code=000002; JSESSIONID-FANG=FD6178335901E442DE30A3662D4D90EE; JSESSIONID=%s; proLEYOUJIA=YjI3ZTY0OTktOWY5OS00ZmVlLWJlYWUtMTZjMTk2ZGMwZWI4; login-workerid=06045224'% (jjshome_uuid_value,_smt_uid_value, jjshome_sid_value,JSESSIONID)
    print('cookie===',cookie)


    # 将中文转换格式为URL编码，方便接口调用
    aa = [name,xm]
    bb = []
    for i in aa:

        cc = urllib.parse.quote(i)
        bb.append(cc)

    print(bb)
    nowtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(nowtime)

    body2 = "opWorkerId=%s&queryPurview=&pageNum=1&pageSize=100&deptName=%s&deptNumber=5501462&workerName=%s&workerId=%s&scopeType=5&userTypeStr=&timeType=1&startTime=%s&endTime=%s" %(empnumber,bb[0],empnumber,bb[1],nowtime,nowtime)
    print('body2=',body2)


    headers2 = {
        'Host': 'i.leyoujia.com'
        ,'Connection': 'keep-alive'
        ,'Content-Length': '236'
        ,'Pragma': 'no-cache'
        ,'Cache-Control': 'no-cache'
        ,'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"'
        ,'Accept': 'application/json, text/javascript, */*; q=0.01'
        ,'X-Requested-With': 'XMLHttpRequest'
        ,'sec-ch-ua-mobile': '?0'
        ,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        ,'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        ,'Origin': 'https://i.leyoujia.com'
        ,'Sec-Fetch-Site': 'same-origin'
        ,'Sec-Fetch-Mode': 'cors'
        ,'Sec-Fetch-Dest': 'empty'
        ,'Referer': 'https://i.leyoujia.com/attend/main/index'
        ,'Accept-Encoding': 'gzip, deflate, br'
        ,'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,'
        ,'Cookie':cookie
    }

    response2 = requests.request('post', url2, data=body2, headers=headers2, verify=False)
    print(response2.text)
    print('----------------------------------------')
    lists = json.loads(response2.text)['data']['list']
    print(lists)


    WDK_name=[]
    hh = time.strftime('%H', time.localtime(time.time()))
    print(hh)
    if int(hh)<12:
        # 上班
        for i in lists:
            if i['upAttendStatusStr']=='旷工':
                WDK_name.append(i['workerName'])

            else:
                pass
        print('请通知同事打上班卡')
    else:

        #下班
        for i in lists:
            if i['nextAttendStatusStr']=='旷工':
                WDK_name.append(i['workerName'])

            else:
                pass
        print('请通知同事打下班卡')


    print('WDK_name====',WDK_name)
    return WDK_name



#发送邮件函数
def Email(WDK_name):


    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    title = info
    #(",".join(str(i) for i in WDK_name  去列表数据并用逗号分割)
    content = '跟新时间：'+response_time+'\n'+'通知：\n      '+info+':\n      '+",".join(str(i) for i in WDK_name)
    # content = response_time+u'    成交列表响应时间为%s秒，请通知开发及时处理'%WDK_name
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="ffkzjccrdtmsjhhe" # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers =['袁猛<1093040152@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = title  #主题
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


def main(WDK_name):


    # 有同事未打卡发送邮件
    if len(WDK_name) == 0:
        print('同事都已打卡，不进行通知')
    else:
        Email(WDK_name)



global wechat_lock
wechat_lock = Lock()

# 这里可以设置UIDS, 多个人可同时接收 [袁猛，李良，蔡姻，张斯杰，罗柳]
UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m','UID_7zDNlQLoP6BwAJFJ6dRCuy9EQ1fp','UID_dxNzj6aupA6Q4QZrDkwmCcDLMX2e','UID_nSMBON6ECkBvdpOC3QeUfIUb7tJX','UID_pyB3i43mzt2LctecgCBZWBz035GZ']
# UIDS = ['UID_j0EdePPCONxX3OszmdyvwSYknX8m']

APP_TOKEN = 'AT_wW7eEobXR61htcs4zw6HIchK1yUaSx8L'
# AT_zueTbAm3qrDJy2BvWtYwJwqVgRjGZIhF

class wechat_thread(Thread):
    """
    采用线程方式，不阻塞
    """

    def __init__(self, uids: list, content: str, topic_ids: list = [], url: str = '', app_token=''):

        # text：消息标题，最长为256，必填。
        # desp：消息内容，最长64Kb，可空，支持MarkDown。

        super(wechat_thread, self).__init__(name="wechat_thread")
        self.request_url = "http://wxpusher.zjiecode.com/api/send/message"
        self.uids = uids
        self.content = content
        self.topic_ids = topic_ids
        self.url = url
        self.lock = wechat_lock
        self.app_token = app_token if len(app_token) > 0 else APP_TOKEN

    def run(self):
        if self.content is None or len(self.content) == 0:
            return
        params = {}
        params['appToken'] = self.app_token
        params['content'] = self.content
        params['contentType'] = 1
        params['topicIds'] = self.topic_ids
        params['uids'] = self.uids
        params['url'] = self.url

        # 发送请求
        try:
            response = requests.post(self.request_url, json=params).json()
            if not response.get('success', False):
                print(response)
        except Exception as e:
            print("{} wechat_thread sent failed! ex:{},trace:{}".format(datetime.now(), str(e), traceback.format_exc()),
                  file=sys.stderr)
            return

        print("wechat_thread sent successful!")


def send_wx_msg(*args, **kwargs):
    """
    发送微信Msg
    :param content:   发送内容
    :return:
    """
    content = kwargs.get('content', None)
    if content is None:
        if len(args) == 0:
            return
        content = args[0]
    if len(content) == 0:
        return


    if not isinstance(content, str):
        if isinstance(content, dict):
            content = '{}'.format(print_dict(content))
        else:
            content = str(content)

    uids = kwargs.get('uids', [])
    # 没有配置的话，使用缺省UID
    if len(uids) == 0:
        uids.extend(UIDS)

    app_token = kwargs.get('app_token')

    t = wechat_thread(uids=UIDS, content=content, app_token=APP_TOKEN)
    t.daemon = False
    t.start()

if __name__ == '__main__':
    hh = time.strftime('%H', time.localtime(time.time()))
    print(hh)
    if int(hh) < 12:
        info = '请告知以下同事打上班卡'
    else:
        info = '请告知以下同事打下班卡'
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    name = '测试部'
    xm = '袁猛'
    empnumber = '06045224'
    empno = '252613'
    password = 'mm711232'
    url = 'https://coa.leyoujia.com/aicp/mainremote'
    url2 = 'https://i.leyoujia.com/attend/main/doAttendList'
    WDK_name = CJ_list(empno, url, empnumber, name, url2, xm)

    main(WDK_name)

    # (",".join(str(i) for i in WDK_name  去列表数据并用逗号分割)
    text = '通知：'+response_time+'\n\n    '+info+':\n    '+"\n    ".join(str(i) for i in WDK_name)

    send_wx_msg(text)


