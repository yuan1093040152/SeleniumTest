# coding=utf-8
"""
@Author  : Yuan Meng
@File    : onlineHtList.py
@Time   : 2026/4/2 15:23
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import json

import requests
htbh = '58000328646'
cookie = 'accTyp=1;lyj_pc_token=UzoKyXqUHRrDdhIckvYV81HwcbPdXZx0;proLEYOUJIA=M2E4ODk1YmUtNWMyMC00NmU5LWE0NmQtZjM3ODFmY2IyMWE5;JSESSIONID=93D09E036FD57AF045761EA9ADC3DB19;jjshome_uuid=a5b00b9b-8eeb-9768-0482-d4c83eb96712;login-workerid=06045224;login-mac=dc02f04c52b58e4751f9223b9d2fe776;jjshome_sid=afe9b5a1-336e-2b38-a4ab-a7808da5bd31'
def htlist(cookie,htbh):
    url = "https://i.leyoujia.com/jjsht/htMainListNew"
    payload="pageSize=25&currPage=1&workerType=&workerId=&qyfzrId=&managerType=&htbh=%s&gzdh=&signInfo=&signTel=&ywlx=&xylx=&statusArr=&approvalStatus=&htlx=&dateType=&dateS=&dateE=&platform=&keyWord="%(htbh)
    headers = {
    'cookie':cookie,
    'content-type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

def extract_contract_info():
    data = htlist(cookie,htbh)
    results = []
    # 获取合同列表
    data = json.loads(data)
    contract_list = data.get("data", {}).get("list", [])
    if not contract_list:
        print("未找到合同数据")
        return results

    # 提取每个合同的指定字段
    for contract in contract_list:
        extracted = {
            "id": contract.get("id"),
            "htms": contract.get("htms"),
            "htbh": contract.get("htbh"),
            "gzdh": contract.get("gzdh"),
            "signInfo": contract.get("signInfo"),
            "platformStr": contract.get("platformStr"),
            "wymc": contract.get("wymc"),
            "djr": contract.get("djr"),
            "statusStr": contract.get("statusStr"),
            "fhid": contract.get("fhid"),
            "djrq": contract.get("djrq"),
            "completeTime": contract.get("completeTime")
        }
        results.append(extracted)
    return results

def print_contract_info(contracts):
    if not contracts:
        print("暂无合同数据")
        return

    for idx, contract in enumerate(contracts, 1):
        print(f"\n{'=' * 50}")
        print(f"合同 {idx}")
        print(f"{'=' * 50}")
        id = {contract['id']}
        id = list(id)[0]
        print(f"合同ID",id)
        print(f"合同名称: {contract['htms']}")
        print(f"合同编号: {contract['htbh']}")
        print(f"成交单号: {contract['gzdh']}")
        print(f"签约人: {contract['signInfo']}")
        print(f"供应商: {contract['platformStr']}")
        print(f"房屋名称: {contract['wymc']}")
        print(f"登记人: {contract['djr']}")
        print(f"合同状态: {contract['statusStr']}")
        print(f"房号ID: {contract['fhid']}")
        print(f"生成日期: {contract['djrq']}")
        print(f"签署完成时间: {contract['completeTime']}")
    return id


# 提取信息
contracts = extract_contract_info()
# 打印结果
print_contract_info(contracts)