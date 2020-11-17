#coding=utf-8
from selenium import webdriver
from email.mime.text import MIMEText
import requests,json,urllib3,time,smtplib
import urllib.parse

def login_im(empno,url):
    body = 'msgBody={"imei":"pcMac-6C0B84A472DD","mac":"6C0B84A472DD,3035323042363737313642304135434620202020,204153594EFF,","lat":0,"lng":0,"ipStr":"172.16.9.54","loginAddr":"","username":"c4jG93780l8r","password":"21218cca77804d2ba1922c33e0151105","empNo":"087394","appVer":"2.3.3.1","sysVer":"6.1.7601","env":"online"}'
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

def CJ_list(empno,url,empnumber,name,url2):
    url_all = login_XXT(empno,url,empnumber)

    # 使用cookie登录并获取页面cookie
    driver = webdriver.Chrome()
    driver.get(url_all)
    time.sleep(1)
    cookie = driver.get_cookies()
    print(cookie)
    SESSION = cookie[0]['name']
    SESSION_value = cookie[0]['value']

    jjshome_sid = cookie[1]['name']
    jjshome_sid_value = cookie[1]['value']

    _smt_uid = cookie[2]['name']
    _smt_uid_value = cookie[2]['value']

    jjshome_uuid = cookie[3]['name']
    jjshome_uuid_value = cookie[3]['value']

    JSESSIONID = cookie[6]['name']
    JSESSIONID_value = cookie[6]['value']

    print('JSESSIONID:', JSESSIONID)
    print('JSESSIONID_value:', JSESSIONID_value)
    print('------------------------------')
    print('jjshome_uuid:', jjshome_uuid)
    print('jjshome_uuid_value:', jjshome_uuid_value)
    print('------------------------------')
    print('jjshome_sid:', jjshome_sid)
    print('jjshome_sid_value:', jjshome_sid_value)
    print('------------------------------')
    print('SESSION:', SESSION)
    print('SESSION_value:', SESSION_value)
    print('------------------------------')

    driver.close()
    driver.quit()

    # workerId = '77806702'
    # workerName1 = '测试营销副总裁'

    # 将姓名转换格式，方便接口调用
    workerName = urllib.parse.quote(name)
    print(workerName)

    body2 = "importErrorStr=&currPage=1&pageSize=100&workerType=0&workerId=%s&workerName=%s&dateType=1&dateS=&dateE=&cjTypeStr=&jdzt=&jyzt=&gzdh=&zlsqType=1&ywjd=&khly=&wymc=&yzxm=&jjfw=&fybh=&qdbz=&cwbz=&provinceId=&cityId=&areaId=&unpaymentS=&unpaymentE=&unpayment=0&sxyq=0&isJrgx=0&fxd=0&ycd=0&ykfp=0&hjStatus=0&ssStatus=0&cfStatus=0&wsygh=0&ishtyd=0&istsd=0&isGlGzdh=0&sfsjd=0" % (
    empnumber, workerName)

    headers2 = {
        'Host': 'i.leyoujia.com',
        'Connection': 'keep-alive',
        'Content-Length': '389',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Origin: https':'//i.leyoujia.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        # 'Referer: https':'//i.leyoujia.com/jjscj/index',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'jjshome_uuid=%s; _smt_uid=5eea41d2.29c10598; SESSION=%s; jjshome_sid=%s; JSESSIONID=%s' % (
        jjshome_uuid_value, SESSION_value, jjshome_sid_value, JSESSIONID_value)
    }

    response2 = requests.request('post', url2, data=body2, headers=headers2, verify=False)
    print(response2.text)
    print('----------------------------------------')
    rs_time = response2.elapsed.total_seconds()
    print(rs_time)
    return rs_time


#发送邮件函数
def Email(rs_time):
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    content = response_time+u'    成交列表响应时间为%s秒，请通知开发及时处理'%rs_time
# 第三方 SMTP 服务
    mail_host="smtp.qq.com" #设置服务器
    mail_user="1093040152@qq.com" #用户名
    mail_pass="wcmynglgfomygecd" # QQ邮箱登录的授权码
    # receivers =['袁猛<1093040152@qq.com>','袁猛<yuanm@leyoujia.com>','齐红宁<qhn@leyoujia.com>','石进<shij@leyoujia.com>']
    receivers =['袁猛<1093040152@qq.com>','周进玲<1827973168@qq.com>','李良<1551023261@qq.com>','左超<97275389@qq.com>','谢银艳<173580375@qq.com>']
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(content, 'plain', 'utf-8') #文本内容
    message['From'] ='袁猛<1093040152@qq.com>' #mail_user # 发送者   （发送人同QQ备注，可不写）
    message['To'] = ','.join(receivers) # 这里必须要把多个邮箱按照逗号拼接为字符串
    subject = content  #主题
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

    """
    测试营销副总裁   77806702    087394   888888   
    """
    response_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(response_time)
    name = '测试营销副总裁'
    empnumber = '77806702'
    empno = '087394'
    password = '888888'
    url = 'https://coa.leyoujia.com/aicp/mainremote'
    url2 = 'https://i.leyoujia.com/jjscj/index/cjIndexList'
    rs_time = CJ_list(empno,url,empnumber,name,url2)
    code = response_time+'     成交列表页面响应时间:' + str(rs_time) + 's'

    #超过2秒发送邮件
    if rs_time < 2 :
        print(code)
    else:
        Email(rs_time)

