#coding=utf-8
from selenium import webdriver
from email.mime.text import MIMEText
import requests,json,urllib3,time,smtplib
import urllib.parse

def login_im(empno,url):
    body = 'msgBody={"imei":"pcMac-6C0B84A472DD","mac":"6C0B84A472DD,3035323042363737313642304135434620202020,204153594EFF,","lat":0,"lng":0,"ipStr":"172.16.9.54","loginAddr":"","username":"c4jG93780l8r","password":"21218cca77804d2ba1922c33e0151105","empNo":"087394","appVer":"2.2.1.0","sysVer":"6.1.7601","env":"online"}'
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
    url_all="https://172.16.22.100/jjslogin/forward?id=%s"%token1
    print(url_all)
    return url_all

def CJ_list(empno,url,empnumber,name):
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

    JSESSIONID = cookie[4]['name']
    JSESSIONID_value = cookie[4]['value']

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


if __name__ == '__main__':

    """
    测试营销副总裁   77806702    087394   888888   
    """

    name = '测试营销副总裁'
    empnumber = '77806702'
    empno = '087394'
    password = '123456'
    url = 'http://172.16.22.100/aicp/mainremote'
    url2 = 'https://172.16.22.100/jjscj/index/cjIndexList'
    login_im(empno, url)


