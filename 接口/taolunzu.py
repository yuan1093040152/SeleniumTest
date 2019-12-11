#codingutf-8
import requests
def aa():
	for i in range(2,101):
		url = 'https://coa.leyoujia.com/aicp/mainremote'

		data = "msgBody=%7B%22groupName%22%3A%22"+"test"+str(i)+"%22%2C%22workerNos%22%3A%22252613%2C129130%2C203228%2C330813%22%2C%22owner%22%3A%22252613%22%2C%22workerId%22%3A%2206045224%22%2C%22imei%22%3A%22pcMac-6C0B84A472DD%22%7D"
# %E8%A2%81%E7%8C%9B%20(%E6%B5%8B%E8%AF%95%E9%83%A8)%E7%AD%89
		# data1 = {
		# 	"groupName":"test001",
		# 	"workerNos":"252613,203228,330813",
		# 	"owner":"252613",
		# 	"workerId":"06045224",
		# 	"imei":"pcMac-6C0B84A472DD"
		# }

		headers = {
			'appname': "pc-im",
			'deptname': "%25E6%25B5%258B%25E8%25AF%2595%25E9%2583%25A8",
			# %25E6%25B5%258B%25E8%25AF%2595%25E9%2583%25A8
			'deptnumber': "5501462",
			'empname': "%25E8%25A2%2581%25E7%258C%259B",
			# %25E8%25A2%2581%25E7%258C%259B
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
			'postman-token': "f75e59fb-f1b1-9d83-5865-ae4aadff101e"
		}
		response = requests.request("POST", url, data=data, headers=headers)

		print(response.text)
		# print (type(response.text))

aa()