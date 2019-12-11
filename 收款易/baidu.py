from selenium import webdriver

import time,login,loginyes,quit


driver = webdriver.Firefox()
	
driver.get("http://www.maiyanx.com/")

login.login(driver)

loginyes.loginyes(driver)

quit.quit(driver)

print ("Hello World")

