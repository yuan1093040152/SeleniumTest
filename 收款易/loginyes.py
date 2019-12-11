import time
def loginyes(driver):

	title = driver.title
	print (title)
	if title == u"后台管理中心":
	   print ("用例执行成功")
	   
	else:
	     print ("用例执行失败")
	# time.sleep(3)
	driver.implicitly_wait(30)
	     
	now_url = driver.current_url
	print (now_url)
	     
	if now_url == u"http://skytest.hzxun.com/index.php/Admin/Index/index.html":
	   print ("url正确")
	   
	else:
	   print ("url错误") 
	   
	# time.sleep(3)
	driver.implicitly_wait(30) 
	driver.find_element_by_link_text("退出登录").click()
	time.sleep(3)
