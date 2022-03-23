#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2022/3/10 19:22
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import re

a = ['jjshome_uuid=48a2b06d-ee49-ce32-5fd7-5858302d8691', ' _smt_uid=607e8056.269f8a49', ' cookiesId=449898cb860d4d00a0cea2a58b1c7896', ' gr_user_id=94fac31f-e0ec-4263-aac9-2e33292eb1f6', ' lyj_analysis_pageCookie=1008%3A3', ' _ga=GA1.2.1568699102.1620269846', ' /hsl/house/house-detail_guidance=1', ' agentCardhd_time=1', ' ysl-list=1', ' reserve-list=1', ' /community/communityDic/communityDic-list_guidance=1', ' /hsl/index/house-list_guidance=1', ' Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1623815443,1625534400', ' Hm_lvt_728857c2e6b321292b2eb422213d1609=1623815443,1625534400', ' /hsl/entrust/entrust-add_guidance=1', ' fhListCookies=', ' iJSESSIONID=22B6B193D39653DD6C34ED35B07C5819', ' JSESSIONID-NEWSYS=D0223F8B30E607172ABCC25078942640', ' uatLEYOUJIA=MzRkMjYwNzEtMTAxZC00OWIwLTk2YWMtOTUyODVkZTE0YTIw', ' testLEYOUJIA=NDNhYjJiNDMtZTBmMy00NTc1LWE3ODMtYTA3NTFjNDNiMzEx', ' login-mac=6C-0B-84-04-4D-E6', ' jjshome_sid=22557e2b-ee9b-d9c4-b8a7-545ac30540e8', ' JSESSIONID=76C82CF007968F648A7B99134215A60E', ' proLEYOUJIA=NDJjMGQxZDMtMzgwOS00OWUxLWI3YzQtOWNkZWQ5NDAzOTJj', ' login-workerid=77806698']

b = {}
for i in a:
    if 'jjshome_uuid' in i:
        strlist = i.split('=')
        # print(strlist)
        b[strlist[0]] = strlist[1]

    elif 'jjshome_sid' in i:
        strlist = i.split('=')
        # print(strlist)
        b[strlist[0]] = strlist[1]

    elif 'uatLEYOUJIA' in i:
        strlist = i.split('=')
        # print(strlist)
        b[strlist[0]] = strlist[1]

# print(b)
try:
    cd = 'jjshome_uuid=%s;uatLEYOUJIA=%s;jjshome_sid=%s'%(b['jjshome_uuid'],b[' uatLEYOUJIA'],b[' jjshome_sid'])
    print(cd)
except:
    pass




