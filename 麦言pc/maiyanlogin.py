import time

def login(driver):

	# driver.find_element_by_xpath("/html/body/div[3]/p").clink()

	driver.implicitly_wait(30)
	# time.sleep(5)

	# driver.find_element_by_class_name("poster-btn").clink()

	time.sleep(5)

	driver.find_element_by_class_name("btn-normal").click()

	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[2]/input").clear()

	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[2]/input").send_keys("guo")

	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[3]/input").clear()

	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[3]/input").send_keys("123456")

	driver.find_element_by_name("net_auto_login").click()

	driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[5]").click()

	driver.find_element_by_id("header_publish").click()

	driver.implicitly_wait(30)

	now_url = driver.current_url

	print (now_url)
	     
	if now_url == u"http://www.maiyanx.com/publish/":

	   print ("url正确,登录成功")
	   
	else:
	   print ("url错误,登录失败") 