#coding=utf-8
import requests

url = "https://coa.leyoujia.com/aicp/mainremote"
i = 37
for x in range(70):
     
    payload = "serviceCode=40002&methodCode=50001&msgBody=%7B%22groupName%22%3A%22%E8%A2%81%E7%8C%9B%20(%E6%B5%8B%E8%AF%95%E9%83%A8)%E7%AD%89"+str(i)+"%22%2C%22workerNos%22%3A%22252613%2C203228%22%2C%22owner%22%3A%22252613%22%2C%22workerId%22%3A%2206045224%22%2C%22imei%22%3A%22pcMac-6C0B84A472DD%22%7D"
    headers = {
        'appname': "pc-im",
        'deptname': "%25E6%25B5%258B%25E8%25AF%2595%25E9%2583%25A8",
        'deptnumber': "5501462",
        'empname': "%25E8%25A2%2581%25E7%258C%259B",
        'empno': "252613",
        'empnumber': "06045224",
        'imei': "pcMac-6C0B84A472DD",
        'methodcode': "50001",
        'origin': "app://im.leyoujia.com",
        'servicecode': "40002",
        'token': "04809ec3d94008a5d653e1b93d90e5ca",
        'v': "3",
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "01cee136-10a5-e154-6d0e-1a63a9d6f449"
        }

    response = requests.request("POST", url, data=payload, headers=headers,verify = False)

    print(response.text)
    i = i+1