#coding=utf-8
import threading,time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

def aaa(url,name):    #用例
	driver = webdriver.Chrome()
	driver.get(url)
	# driver.maximize_window()
	driver.implicitly_wait(30)
	driver.find_element_by_name("userName").send_keys(name)
	driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
	driver.find_element_by_id("password").send_keys("1")
	driver.find_element_by_id("login_button").click()
	time.sleep(3)
	driver.close()
	# time.sleep(3)

def bbb(url,name1):   #用例
	driver = webdriver.Chrome()
	driver.get(url)
	# driver.maximize_window()
	driver.implicitly_wait(30)
	driver.find_element_by_name("userName").send_keys(name1)
	driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
	driver.find_element_by_id("password").send_keys("1")
	driver.find_element_by_id("login_button").click()
	time.sleep(3)
	driver.close()
	# time.sleep(3)


if __name__ == "__main__":
	for x in xrange(1):
    	# pass:
    	#设置参数
		url = 'http://172.16.3.100/jjslogin/index'
		name = u'谭当飞'
		name1 = u'袁猛'
		# 创建线程并存入数组
		t = threading.Thread(target=bbb,args=(url,name1))
		t1 = threading.Thread(target=aaa,args=(url,name))
		# t.setDaemon(True)
		t.start()
		t1.start()
	t.join()      #当所有线程执行完才执行主进程
	print (u'执行完')   