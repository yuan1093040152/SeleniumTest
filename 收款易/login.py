import time
def login(driver):
	
	driver.find_element_by_name("username").clear()
	driver.find_element_by_name("username").send_keys("admin")
	driver.find_element_by_name("password").clear()
	driver.find_element_by_name("password").send_keys("123456")
	time.sleep(3)
	driver.find_element_by_name("submit").click()
	time.sleep(3)
	