#coding=utf-8
import requests,json,urllib,time,random,re
from tqdm import tqdm, trange

# 直接postman请求复制代码过来
url = "http://api.gifshow.com/rest/n/feed/hot"
querystring = {"mod":"OPPO(OPPO R9s)",
	"lon":"114.099347",
	"country_code":"cn",
	"extId":"06d4a571056fb092847520aecb14bd3d",
	"did":"ANDROID_78688703ba74a989",
	"app":"0",
	"net":"WIFI",
	"oc":"UNKNOWN",
	"ud":"392602400",
	"c":"OPPO",
	"sys":"ANDROID_6.0.1",
	"appver":"5.9.3.6975",
	"ftt":"",
	"language":"zh-cn",
	"iuid":"DunOZstEyWebOC+4bVgTRstNutXpEYtEmA9zWBcCI0s4b/5jY/r0Okb3oCmURMPjsO7AbdLEYcFPJzCfdIgnSYyA",
	"lat":"22.562575",
	"ver":"5.9",
	"max_memory":"256"
	}
payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n7\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"page\"\r\n\r\n2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"coldStart\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"count\"\r\n\r\n20\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pv\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"id\"\r\n\r\n628\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"refreshTimes\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pcursor\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"source\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__NStokensig\"\r\n\r\nfef41e66f464b329c02b59a3027b86748f7fe75ac1969d6faea9838f67e3a4e2\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"token\"\r\n\r\n84f6cb3a631a4343bf6f6048213be68c-392602400\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_key\"\r\n\r\n3c2cd3f3\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"os\"\r\n\r\nandroid\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n0ec218adf71ae8e530947a8077e53605\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "b9e34fdd-242a-d013-cfe0-1ca8c1d88da4"
    }
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
# print(response.text)
dict = json.loads(response.text)
# print (dict)
all_url = dict['feeds']
print (len(all_url))
for x in all_url:
	try:
		name = x['caption']
		mv_url = x['main_mv_urls'][0]['url']
		print (name)
		print (mv_url)		
	except:
		pass

	try:
		# b = random.randint(10000,99999)
		# path = 'E:\\test\\'+'test_'+str(b)+'.mp4'
		path = u'E:\\test\\'+name+'.mp4'				
		file = urllib.urlopen(mv_url).read()			
		f = open(path,'wb')
		f.write(file)
		for i in trange(100):
			time.sleep(0.01)
			pass
		time.sleep(5)
		f.close()
		
	except :
		pass
		
	




