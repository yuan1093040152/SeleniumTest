# coding=utf-8
"""
@Author: Yuan Meng
@File: test016.py
@Time: 2026/5/13 22:17
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D 分屏
Ctrl+/ 快速注释

"""
import subprocess
import json

import requests


def cjlist_accurate():
    url = "https://i.leyoujia.com/jjscj-deal/index/cjIndexList"

    # 使用从浏览器复制的完整 headers
    headers = {
        'content-type': 'application/json',
        'cookie': 'jjshome_uuid=17ba35ec-9032-5667-970e-762d7bcd3496; prefs={}; fhListCookies=; gr_user_id=cff45c57-2c71-4a02-8138-82e7894de66c; cookiesId=7f2b44a078c34dc18d6ac70f44aa728f; userInfoCookie=bC3nvfu4XquEcf2F5XZgdZxuWGLDRydSQSX3co-BZr2o6tzvjPURDw-gIvl04w22AoLfMCGX781Z-J67PDeksPRcrWB8upERzxkwT0cJV1I=1; agentCardhd_time=1; token=t.RgsYudEC8r4CuGfqPXtA; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1774527206,1776391025; Hm_lvt_728857c2e6b321292b2eb422213d1609=1774527206,1776391025; login-workerid=06045224; login-mac=dc02f04c52b58e4751f9223b9d2fe776; JSESSIONID=F34BFF000BF4F3E013F5530F6D6D41AB; accTyp=1; proLEYOUJIA=M2M1MDcwNTgtNWQzZC00MmM2LTllOTktZWJhYjA1NWY5MDQy; __session:0.05605370019726297:_dgHidden=false; jjshome_sid=88774264-2137-053e-d8c2-2ebaec695ada',  # 从 cURL 中复制完整 cookie
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',  # 很可能就是这个！
        'referer': 'https://i.leyoujia.com/jjscj-deal/index/cjIndexList',
        'origin': 'https://i.leyoujia.com',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    # 请求体保持和浏览器完全一致
    inner_params = {
        "pageSize": 100,
        "currPage": 1,
        "workerType": 0,
        "workerId": None,
        "managerTypeVal": 3,
        "dateType": 1,
        "dateS": None,
        "dateE": None,
        "orderTab": 1,
        "managerType": 3,
        "cjTypeStr": None,
        "jdztArr": [],
        "jyztArr": [],
        "gzdh": "M1112605-4806",  # 你的工单号
        "unpayment": 0,
        "sxyq": 0,
        "isJrgx": 0,
        "fxd": 0,
        "ycd": 0,
        "ykfp": 0,
        "hjStatus": 0,
        "ssStatus": 0,
        "cfStatus": 0,
        "wsygh": 0,
        "istsd": 0,
        "isGlGzdh": 0,
        "sfsjd": 0,
        "sflhd": 0,
        "sdZdjd": 0,
        "isUpdateCommission": 0,
        "isMainChange": 0,
        "isWlyj": 0,
        "yjChangeByGlr": 0,
        "lljf": 0,
        "htXzd": 0,
        "zffsArr": None,
        "slfsArr": None,
        "ishdlk": None,
        "zlsqType": 1,
        "zlsqValue": None,
        "mainRele": {"ywjdSydkDkfs": None},
        "ywjdArr": None,
        "fxCompanyId": None,
        "taskNodeTypeStr": None,
        "useHtTypes": None,
        "rgsZtArr": [],
        "hasUseHt": None,
        "companyIdStr": None,
        "hzjgIdStr": None,
        "khly": None,
        "wymc": None,
        "yzxm": None,
        "jjfw": None,
        "fybh": None,
        "qdbz": None,
        "cwbz": None,
        "provinceId": None,
        "cityId": None,
        "areaId": None,
        "fyztArr": None,
        "unpaymentS": None,
        "unpaymentE": None,
        "jdfhStatusArr": None,
        "shqlStatusArr": None,
        "messageYzOrKh": None,
        "messageDayArr": None,
        "dzjeSqMin": None,
        "dzjeSqMax": None,
        "dzjeShMin": None,
        "dzjeShMax": None
    }
    payload = {"key": json.dumps(inner_params, separators=(',', ':'))}
    print("aaaaaaaaaaaaaa----", payload)
    # 关键：使用 data=json.dumps(payload) 并确保 headers 中的 content-type 是 application/json
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    print("完整响应:", json.dumps(data, indent=2, ensure_ascii=False))  # 打印完整响应
cjlist_accurate()