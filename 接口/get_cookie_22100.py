from selenium import webdriver
from aip import AipOcr
import time,requests


def get_cookies(url,username,password):

#登录并获取页面cookie
	driver = webdriver.Chrome()

	driver.get(url)
	time.sleep(3)
	driver.maximize_window()
	

	#截图验证码
	# url_src = driver.find_element_by_id('verify_code')
	# url_src.screenshot('E://test//url_src.png')

	# GetImageCode1 = GetImageCode()

	driver.find_element_by_id('workerStr').clear()
	driver.find_element_by_id('workerStr').send_keys(username)
	time.sleep(2)
	driver.find_element_by_xpath('//a[@class="ui-corner-all"]').click()
	driver.find_element_by_id("password").send_keys(password)

	# driver.find_element_by_xpath("//input[@id='ck_num']").send_keys(GetImageCode1)
	driver.find_element_by_id("login_button").click()
	time.sleep(5)

	cookie = driver.get_cookies()
	print ('----------------------------这是一条分割线----------------------------')
	print ('cookie:',cookie)
	print ('----------------------------这是一条分割线----------------------------')
	_smt_uid = cookie[0]['name']
	_smt_uid_value = cookie[0]['value']
	print (_smt_uid+':'+_smt_uid_value)


	SESSION = cookie[1]['name']
	SESSION_value = cookie[1]['value']
	print (SESSION+':'+SESSION_value)


	JSESSIONID = cookie[2]['name']
	JSESSIONID_value = cookie[2]['value']
	print (JSESSIONID+':'+JSESSIONID_value)

	# SESSION = cookie[3]['name']
	# SESSION_value = cookie[3]['value']
	# print (SESSION+':'+SESSION_value)
	driver.quit()


def GetImageCode():
		APP_ID = '16947930'
		API_KEY = '0ynD0BGPC6QtrPWs68i4sQO9'
		SECRET_KEY = 'fKsckEf41jUtTDBwFIeHYkhnYyvNaViz'
		client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
		print (11)

		with open('E://test//url_src.png','rb') as f:
			image = f.read()
			image1 = client.basicAccurate(image)
			print (image1)
			print (image1['words_result'][0]['words'])
			return image1['words_result'][0]['words']




# if __name__ == "__main__":

# 	# url = 'https://i.leyoujia.com/jjslogin/tologin'
# 	url = 'http://172.16.22.100/jjslogin/tologin'
# 	username = u'袁猛'
# 	password = u'mm711232'
# 	get_cookies(url,username,password)





