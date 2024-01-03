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
               "Cookie":"jjshome_uuid=e3521da2-faa5-fc59-f853-454b445f4cc9; _smt_uid=; cookiesId=116347ef6ac44e45a1c414bf7b790d1b; _ga=GA1.2.1941642435.1637634248; agentCardhd_time=1; token=t.LmX27IZZvGOqM1DRudGm; prefs={}; fhListCookies=; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1640866512; Hm_lvt_728857c2e6b321292b2eb422213d1609=1640866512; gr_user_id=b4d54e60-5a65-41ea-815a-9de61463cd28; proLEYOUJIA=ZDEzZTk4ZWQtMzc0Mi00NTliLTkxYTUtNDY4YTI1Njk2MmE1; JSESSIONID=f10c3d27-47c3-ad52-48c6-0912d406b6df; login-mac=6C-0B-84-A4-72-DD; login-workerid=06045224; jjshome_sid=0CED257DF86775424FC22B6B3AC55A9D",
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
    js(ids,text,title)
