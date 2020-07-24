#coding=utf-8
import urllib.parse

workerId = '12345678'
workerName = '李良'
print(type(workerName))

a=urllib.parse.quote(workerName)
print(a)
#
body2 = "importErrorStr=&currPage=1&pageSize=100&workerType=0&workerId=%s&workerName=%sF&dateType=1&dateS=&dateE=&cjTypeStr=&jdzt=&jyzt=&gzdh=&zlsqType=1&ywjd=&khly=&wymc=&yzxm=&jjfw=&fybh=&qdbz=&cwbz=&provinceId=&cityId=&areaId=&unpaymentS=&unpaymentE=&unpayment=0&sxyq=0&isJrgx=0&fxd=0&ycd=0&ykfp=0&hjStatus=0&ssStatus=0&cfStatus=0&wsygh=0&ishtyd=0&istsd=0&isGlGzdh=0&sfsjd=0"%(workerId,workerName)


# print(body2)

workerName1 = '%E6%9D%8E%E8%89%AF'
print(type(workerName1))