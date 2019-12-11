from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://skytest.hzxun.com/index.php/Admin/Login/login.html")
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("submit").click()
time.sleep(5)
#driver.implicitly_wait(30)
title = driver.title
print (title)
if title == u"后台管理中心":
   print ("用例执行成功")
   
else:
     print ("用例执行失败")
time.sleep(5)
     
now_url = driver.current_url
print (now_url)
     
if now_url == u"http://skytest.hzxun.com/index.php/Admin/Index/index.html":
   print ("url正确")
   
else:
   print ("url错误") 
   
#time.sleep(5)  
driver.implicitly_wait(30) 
driver.find_element_by_link_text("退出登录").click()

driver.quit()