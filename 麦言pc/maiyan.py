from selenium import webdriver

import time

def.login(driver):

	try:
		driver = webdriver.Firefox()
	
		driver.get("http://www.maiyanx.com/")

		driver.find_element_by_class_name("btn-normal").click()

		driver.implicitly_wait(30)

		time.sleep(2)

		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[2]/input").clear()

		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[2]/input").send_keys("guo")

		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[3]/input").clear()

		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[3]/input").send_keys("123456")

		driver.find_element_by_name("net_auto_login").click()

		driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/form/ul/li[5]").click()
		
	except:
		pass

	return

def quit(driver):
	driver.quit

