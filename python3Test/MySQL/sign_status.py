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
import datetime
import json
from datetime import date
from urllib.parse import urlencode
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sendE import Send
import pandas as pd


class ht_status:
	def __init__(self):
		self.Stimes = (date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
		print(self.Stimes)
		self.Etimes =date.today().strftime("%Y-%m-%d")
		print(self.Etimes)
		self.AES_KEY = b"ODcyYTUxNGM1N2M2"
		self.file_path = r'D:\Program Files\已签署待签约数据.xlsx'

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
				"pageSize": 500,
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
				"dateS": self.Stimes,
				"dateE": self.Etimes,
				"platform": "",
				"keyWord": keyword
			}
		headers = {
			'cookie':self.get_cookie(),
			'content-type': 'application/x-www-form-urlencoded'
		}
		response = requests.request("POST", url, headers=headers, data=urlencode(payload))
		print('response-----------',response)
		data = response.json()
		print('data-------------',data)
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

	def build_query(self, gzdh: str, **overrides) -> dict:
		query = {
			"pageSize": 100,
			"currPage": 1,
			"workerType": 0,
			"managerTypeVal": 3,
			"dateType": 1,
			"orderTab": 1,
			"managerType": 3,
			"gzdh": gzdh,
			"zlsqType": 1,
		}
		query.update(overrides)
		return query

	def _encrypt(self, plain: dict) -> str:
		text = json.dumps(plain, ensure_ascii=False, separators=(",", ":"))
		ct = AES.new(self.AES_KEY, AES.MODE_ECB).encrypt(pad(text.encode(), 16))
		return base64.b64encode(ct).decode()

	def _decrypt(self, cipher: str) -> dict:
		raw = base64.b64decode(cipher.strip())
		plain = unpad(AES.new(self.AES_KEY, AES.MODE_ECB).decrypt(raw), 16)
		return json.loads(plain.decode())

	def cj_index_list(self, query: dict) -> dict:
		URL = 'https://i.leyoujia.com/jjscj-deal/index/cjIndexList'
		HEADERS = {
			"content-type": "application/json;charset=UTF-8",
			"encrypt": "true",
			"referer": "https://i.leyoujia.com/lyj-menu/cj/CJ_NEW?showTab=true&submenu=CJCX",
			"cookie": self.get_cookie(),
		}
		resp = requests.post(URL, json={"key": self._encrypt(query)}, headers=HEADERS, timeout=60)
		resp.raise_for_status()
		return self._decrypt(resp.text)

	def check_jyzt(self, gzdh: str, result: dict) -> list:
		"""jyzt 不符合规则时，将传参的 gzdh 加入 cj_error。"""
		cj_error = []
		if not gzdh:
			return cj_error
		prefix = gzdh[0].upper()
		for item in (result.get("data")).get("list"):
			jyzt = item.get("jyzt", '')
			gzdh = item.get('gzdh', '')
			wymc = item.get('wymc', '')
			htbh = item.get('htbh', '')
			djr = item.get('djr', '')
			zdr = item.get('zdr', '')
			cjrq = item.get('cjrq', '')

			print("gzdh:",gzdh,"jyzt:", jyzt)
			if prefix == "M" and jyzt != 1:
				cj_error.append({
        'gzdh': gzdh,
		'jyzt': jyzt,
        'wymc': wymc,
        'htbh': htbh,
        'djr': djr,
        'zdr': zdr,
        'cjrq': cjrq
    })
				break
			if prefix == "Z" and jyzt != 4:
				cj_error.append({
        'gzdh': gzdh,
		'jyzt': jyzt,
        'wymc': wymc,
        'htbh': htbh,
        'djr': djr,
        'zdr': zdr,
        'cjrq': cjrq
    })
				break
		return json.dumps(cj_error)

	def batch_cjlist(self):
		cjdhlist = self.batch_htlist()
		# cjdhlist = ['Z3332606-03490', 'M3072607-0041']
		print("-----------  2天内已签署合同的成交单号  -----------")
		print(cjdhlist)
		print("-----------  数据比对  -----------")
		for gzdh1 in cjdhlist:
			result = self.cj_index_list(self.build_query(gzdh1))
			cj_error = self.check_jyzt(gzdh1, result)
		print("--- 合同已签署但成交交易状态还为待签约的数据 ---")
		print(cj_error)
		return cj_error

	def insertE(self):
		cj_error = self.batch_cjlist()
		# 定义要取的字段和对应的中文名
		fields = ['gzdh', 'jyzt', 'wymc', 'htbh', 'djr', 'zdr', 'cjrq']
		headers = ['成交单号', '交易状态', '物业名称', '合同编号', '登记人', '主单人', '成交日期']
		# 提取数据
		data = []
		for item in cj_error:
			row = [item.get(field, '') for field in fields]
			data.append(row)

		# 创建DataFrame
		df = pd.DataFrame(data, columns=headers)

		# 写入Excel
		with pd.ExcelWriter(self.file_path, engine='openpyxl', mode='w') as writer:
			df.to_excel(writer, sheet_name='已签署待签约数据', index=False)

		print(f"✅ 成功写入 {len(df)} 条数据")
		a = Send()
		a.send_qq_email(title='已签署合同成交单异常状态数据', info=cj_error)

	# def sendEmail(self):
	# 	cj_error = self.batch_cjlist()
	# 	nowtime = datetime.datetime.now()
	# 	a = Send()
	# 	a.send_qq_email(title='已签署合同成交单异常状态数据', info=cj_error)

if __name__ == '__main__':
	ht_status().insertE()
