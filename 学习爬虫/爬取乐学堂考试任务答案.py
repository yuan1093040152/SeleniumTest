#=coding=utf-8
from bs4 import BeautifulSoup
import requests,urllib,time,random,bs4,re,json
from xlutils.copy import copy 
import xlrd,xlwt



url = "https://coa.leyoujia.com/aicp/mainremote"

payload = "msgBody=%7B%22empNo%22%3A%22252613%22%2C%22empNumber%22%3A%2206045224%22%2C%22taskId%22%3A%226038%22%7D&methodCode=50049"
headers = {
    'accept-encoding': "gzip",
    'user-agent': "okhttp/3.2.0",
    'content-length': "120",
    'content-type': "application/x-www-form-urlencoded",
    'appname': "android-ssk",
    'deptname': "%E6%B5%8B%E8%AF%95%E9%83%A8",
    'deptnumber': "5501462",
    'empname': "%E8%A2%81%E7%8C%9B",
    'empno': "252613",
    'empnumber': "06045224",
    'imei': "863903030621990",
    'methodcode': "50049",
    'servicecode': "40003",
    'token': "6e9ae87c7d4810d4d5c7e0a23e2fe394",
    'v': "7",
    'connection': "Keep-Alive",
    'host': "coa.leyoujia.com",
    'cache-control': "no-cache",
    'postman-token': "7d3d266a-5a43-6470-eb61-5c91de698bb1"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)
print (response.text)

dict = json.loads(response.text)
# print (dict)