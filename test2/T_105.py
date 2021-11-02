#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/10/19 16:31
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

import  requests,json

url = "http://itest.leyoujia.com/jjslogin/doLoginNew"
headers = {
    "Cookie":"jjshome_uuid=057f3a09-f8a0-58b6-8d68-01f180472e20; _smt_uid=60b5d0e6.39428262; /hsl/index/house-list_guidance=1; /community/communityDic/communityDic-list_guidance=1; /community/communityDic/communityDic-detail_guidance=1; cookiesId=d2e4fc91be424ab3b2df07e38b613d0e; _ga=GA1.2.1218764700.1622787419; agentCardhd_time=1; /hsl/index/own-house-list_guidance=1; /school/schoolInfo/to-schoolList_guidance=1; /school/schoolInfo/school-detail_guidance=1; gr_user_id=de1a9e70-c4f8-43ae-9893-d555511de2e7; default_city_code=000002; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1631600015,1631754143,1631762228,1632466940; Hm_lvt_728857c2e6b321292b2eb422213d1609=1631600015,1631754143,1631762228,1632466940;/school/schoolInfo/toUpdateInfo_guidance=1; /school/schoolInfo/to-saveSchool_guidance=1; /school/house/house-list_guidance=1; /school/schoolInfo/toUpdateOtherInfo_guidance=1; fhListCookies=; proLEYOUJIA=ZmMwNWM4NWEtMmEwOS00OTlhLWJkMmMtYzJlNDRiZjU2ZDYx; jjshome_sid=b06c17d5-dc6c-c5a1-7413-34e5339e2972; login-workerid=01000098; login-mac=20-6A-8A-81-42-D9,0A-00-27-00-00-00,0A-00-27-00-00-00; iJSESSIONID=41CA5CC1344E148399270040879270BB",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }


data = {

    "workerNo":"000012",
    "wpassword":"123",
    "ckNum":" ",
    "codeVal":"0000",
    "needCkNum":"true",
    "hddid":" ",
    "handInfo":" ",
    "macAddress":"20-6A-8A-81-42-D9,0A-00-27-00-00-00,0A-00-27-00-00-00"
}
# res = requests.post(url=url,data=data1)
# print(res.json())
res = requests.request('post', url, data=data, headers=headers, verify=False)
print(json.loads(res.text))