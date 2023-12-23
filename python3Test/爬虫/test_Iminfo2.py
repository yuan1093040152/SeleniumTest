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
1、利用消息平台发送UAT密码给相关人员
"""
def XXPT_fs(txt,title,emp_number,emp_name):
    url = "https://i.leyoujia.com/msg/im/addTemplateInfo"
    data ={
        "belongDept":"12",
        "laterRemind":"1",
        "pushMode": "1",
        "pushWorker": "2",
        "rank": "1",
        "title": title,
        "type": "1",
        "templateContents": [{"type":"text","value":txt}],

        "templateWorkers": [
                            {"type": "1",
                             "workerType": "1",
                             "value": emp_number,
                             "name": emp_name}
                            ]
    }
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
    return s1


"""
ids:发送的人员   例：[{'06045224': '袁猛'}, {'00410622': '冉成浩'}]
title:发送的标题   
text:发送的内容
"""
def js(ids,text,title):
    for i in ids:
        emp_number = list(i.keys())[0]
        emp_name = list(i.values())[0]
        sendinfo = XXPT_fs(text,title,emp_number,emp_name)
        print(emp_number,emp_name)

if __name__ == "__main__":
    title = 'UAT验收环境登陆密码'
    ids = [{'06045224': '袁猛'}, {'00410622': '冉成浩'}]
    text = '今日UAT验收环境登陆密码为：'
    js(ids,text)
