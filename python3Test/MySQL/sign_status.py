# coding=utf-8
"""
@Author: Yuan Meng
@File: sign_status.py
@Time: 2026/5/19 20:11
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D 分屏
Ctrl+/ 快速注释

"""
import json
from datetime import date
from urllib.parse import urlencode
import requests
from traits.trait_types import self


class ht_status:
	def __init__(self):
		self.times =date.today().strftime("%Y-%m-%d")

	def get_cookie(self):
		"""获取cookie文件内容"""
		cookie_path = r"C:\Users\Administrator\.openclaw\plugin-skills\leyoujia-dzht\scripts\cookie.txt"
		try:
			with open(cookie_path, 'r', encoding='utf-8') as f:
				co =  f.read().strip()
				return co
		except FileNotFoundError:
			print(f"Cookie文件不存在: {cookie_path}")
			return None
		except Exception as e:
			print(f"读取cookie失败: {e}")
			return None


	def htlist(self,ywlx,keyword):
		url = "https://i.leyoujia.com/jjsht/htMainListNew"
		payload = {
				"pageSize": 25,
				"currPage": 1,
				"workerType": "",
				"workerId": "",
				"qyfzrId": "",
				"managerType": "",
				"htbh": "",
				"gzdh": "",
				"signInfo": "",
				"signTel": "",
				"ywlx": ywlx,
				"xylx": "",
				"statusArr": "8",
				"approvalStatus": "",
				"htlx": "",
				"dateType": 3,
				"dateS": self.times,
				"dateE": self.times,
				"platform": "",
				"keyWord": keyword
			}
		headers = {
			'cookie':self.get_cookie(),
			'content-type': 'application/x-www-form-urlencoded'
		}
		response = requests.request("POST", url, headers=headers, data=urlencode(payload))
		data = response.json()
		return data


	# 定义参数列表
	def batch_htlist(self):
		htlists = []
		params_list = [
			{"ywlx": 1, "keyword": "租赁合同"},
			{"ywlx": 2, "keyword": "二手房买卖及居间服务合同"}
		]
		for param in params_list:
			result = self.htlist(ywlx=param["ywlx"], keyword=param["keyword"])
			for cjdh in result["data"]["list"]:
				cjdh = cjdh["gzdh"]
				htlists.append(cjdh)
		return htlists


	def cjlist(self,gzdh):
		url = "https://i.leyoujia.com/jjscj-deal/index/cjIndexList"
		inner_params  = {
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
        "gzdh": gzdh,  # 你的工单号
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
		# 包装成需要的格式
		payload1 = {"key": json.dumps(inner_params, separators=(',', ':'))}
		print("aaaaaaaaaaaaaa----",payload1)
		headers1 = {
			'cookie': self.get_cookie(),
			'content-type': 'application/json; charset=UTF-8',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
			'X-Requested-With': 'XMLHttpRequest',
			'Referer': 'https://i.leyoujia.com/lyj-menu/cj/CJ_NEW?showTab=true&submenu=CJCX',
			'authority': 'true',
			'encrypt': 'i.leyoujia.com',
			'method': 'POST',
			'path': '/jjscj-deal/index/cjIndexList',
			'scheme': 'https',
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'accept-encoding': 'gzip, deflate, br, zstd',
			'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
			'content-length': '1418',
			'priority': 'u=1, i'
		}
		response = requests.request("POST", url, headers=headers1, data=json.dumps(payload1))
		data = response.json()
		print("完整响应:", json.dumps(data, indent=2, ensure_ascii=False))  # 打印完整响应
		return data




	def batch_cjlist(self):
		# cjlists = self.batch_htlist()
		cjlists = ['Z3332605-8542']
		for cjdh in cjlists:
			result = self.cjlist(cjdh)



			# cj_status = result["data"]["list"]
			# for cjstatus in result["data"]["list"]:

				# cj_status = cjstatus["jyzt"]
			# print("-------",cj_status)
				#校验
				# if








if __name__ == '__main__':
	ht_status().batch_cjlist()
