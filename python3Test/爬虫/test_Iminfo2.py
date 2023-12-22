#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/12/22 19:43
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""


import requests
import json

"""
1、获取每日UAT密码
"""
def UAT_pass():
    url = 'http://172.16.3.233:12001/apis/back/oldSystem/PassGet'
    data = {"roomId":"52026368004000"}
    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Host": "172.16.3.233:12001",
        "Origin": "http://172.16.3.233:12001",
        "Pragma": "no-cache",
        "Referer":"http://172.16.3.233:12001/portal/index",
        "sessionID": "zz27wTDemu07bKfdLTXx86c7r27LBC",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    response = requests.post(url,data=json.dumps(data),headers=headers)
    s = response.json()
    return s['msg']

"""
1、登录新系统获取cookie
"""
# def DL():
#     url = "https://i.leyoujia.com/jjslogin/doLoginByImV1"
#     data = {"Accept":"application/json, text/plain, */*",
#             "Accept-Encoding":"gzip, deflate, br",
#             "Accept-Language":"zh-CN,zh;q=0.9",
#             "appName":"pc-im",
#             "Connection":"keep-alive",
#             "Content-Length": "901",
#             "Content-Type": "application/x-www-form-urlencoded",
#             "Cookie": "jjshome_uuid=aeece851-8cf4-acae-e79e-44b66a69fba6; lyj_pc_token=Vme5y9RlmHOkd1gsI0h3ZHUnHU50kKHX; proLEYOUJIA=ODUxYmYzOTYtMzNhNS00ZWI2LWEzOTYtZWYyZTAwZTczYTAw",
#             "Host": "i.leyoujia.com",
#             "imei": "pcMac-80C5484B6EFC",
#             "Sec-Fetch-Dest":"empty",
#             "Sec-Fetch-Mode":"cors",
#             "Sec-Fetch-Site":"none",
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 leyoujiaIm/3.0.6.2",
#             "version":"3.0.6.2"
#             }
#     headres = {"secret":"bD25op4M+n5nlrViLDoYFFNzi3DE+v8Ml5bPQ5Fz0LnmD7vj7CuomccULb/BtjNnCZ7wFvSpU9SQCJNWCkDwcBshqqoBfmYMgIrK6vKUtyjwr2B+AUTJTUTWEbATwluJrHQGQEWJ+fF3rWezDilwPzzlSrahme9h7bhAAYgEWtAsYfDBrYUKXaXSAoUiEPFMXaNTjkA8GdaM0CiFpJ9rQtgChHows0DACZWqZYjNLxDUgMIOPZhLXLqeC5z3KBN6xA++MZ3n1pxHvIagIarT8unjDhA6gFo+rN0sq8MB02aibOyeYzah1r7XrYRCe3mAb6IeZZwtqhVS5MqXWn4FQIXjLKdPOUt5YGpaqo2IxNWBN/5Y2DnknHduUFfZPMBKshxixWLEEcqRlVuvc4reM1CJ68kuGG4xHvz29ql7tvSsOtkFkWtScE6FrZDtwz92k9xmYdon47TufaAWGQ6VVbaMjNrjm95Rzmwyg3MXobj4vjfupO8fwlhJtBc+K0aQWUQZm3NEUmc+VYQLWnNkTckvqYsx2/HQRDVu6qIRXcCHOhAyHKKcL/QNjriHPNP6GD3l1mnqmlDmmfXNdYE4K49t9/Ne0KBsMaQTHOd7uKCSnzRDIr8WgkWBGb2fEWchv7lfnSjEwhqDpF5cAUlnbyPdyEkk6pHMb8dAIhUz5+F7cvQE/k8du2rb5csmw6lrnF7Y9Tca5sIc0O0lj7UnxzVSQLH0NmZko8KwouCHEsiAySxVHWlNdHKp2vvSvUFdRLOeWOHvBRZHxa2hFlnS9LwKJeyoNlNpqedX/lZwSPYR0uieNT1i2PiqmmskRth4sTPEF1JRP9vzJIncz25EZg=="}
#     respose = requests.post(url,headers=headres,data=data)
#     ck = respose.cookies
#     print(ck)



"""
1、利用消息平台发送UAT密码给相关人员
"""
def XXPT_fs(txt,i):
    url = "https://i.leyoujia.com/msg/im/addTemplateInfo"
    data ={
        "belongDept":"12",
        "laterRemind":"1",
        "pushMode": "1",
        "pushWorker": "2",
        "rank": "1",
        "title": "线上密码",
        "type": "1",
        "templateContents": [{"type":"text",
                              "value":txt}],

        "templateWorkers": [

                            {"type": "1",
                             "workerType": "1",
                             "value": i,
                             "name": ""},
                            ]}
    headers = {"Accept":"application/json, text/javascript, */*; q=0.01",
               "Accept-Encoding":"gzip, deflate, br",
               "Accept-Language":"zh-CN,zh;q=0.9",
               "Cache-Control":"no-cache",
               "Connection":"keep-alive",
               "Content-Length":"464",
               "Content-Type":"application/json; charset=UTF-8",
               "Cookie":"prefs={}; fhListCookies=; jjshome_uuid=2d8db24a-d505-94df-befa-fce33a6057be; _ga=GA1.2.469380103.1688031287; /hsl/index/house-list_guidance=1; cookiesId=67fd28febc684aa2b689cff24c43107f; ysl-list=1; reserve-list=1; token=t.ORD0x1QdtR11YEgLgNn0; gr_user_id=3fab8280-a3be-4c3e-bb5d-e2517dd30cd9; connect.sid=s%3A85-aogZtViP5TpwyLIgr5Dfqhj9R0Zb1.%2FdFAOCuSJ4XDikYu6bzsKwowklPrcx62icgEKERUM3g; JSESSIONID-FANG=MWY3Y2IzMDUtNzI2MS00ZWRkLTliMTYtNmQxNGZhZDI3ZDA0; JSESSIONID=8C62D5150084F58A28CB4B8D6072A1D9; proLEYOUJIA=MDJlYzFhOTItMzIzMi00YWRiLWIwNmMtMDdkMzgzYmE3YWE0; login-mac=; jjshome_sid=c6a53232-74a1-7b26-9781-61bc63dd5f5f; login-workerid=33029115; fatLEYOUJIA=N2U5YTIwNTctOTAxNS00ZTYzLWIwYmItNDlmZDkxZDk5MmE2",
               "Host":"i.leyoujia.com",
               "Origin":"https://i.leyoujia.com",
               "Pragma":"no-cache",
               "Referer":"https://i.leyoujia.com/lyj-menu/syssetting/SYS_XXTP?submenu=sent",
               "Sec-Fetch-Dest":"empty",
               "Sec-Fetch-Mode":"cors",
               "Sec-Fetch-Site":"same-origin",
               "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
               "X-Requested-With":"XMLHttpRequest"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    s1 = response.json()
    return s1['success']


# ids = ["袁猛","曾亮","孙杰","苏薇","杨耿晖","李珍一","黄慧","王曼莹","刘颖","冉成浩"]
# ids = ["06045224", "00454949", "06061310", "33029737", "00407662", "00428606", "77807633",  "02081317", "06058331","00410622"]
ids = ["06045224","00410622"]


def js():
    # p1 = UAT_pass()
    txt = '111'
    for i in ids:
        FS_xx = XXPT_fs(txt,i)
        print(FS_xx)

if __name__ == "__main__":
    # DL()
    js()
