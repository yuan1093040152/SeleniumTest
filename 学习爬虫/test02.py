# coding:utf-8
from selenium import webdriver
import time,os,sys,re

	
# 	选择火狐浏览器并打开12306
driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
time.sleep(1)

#出发地定为深圳北
driver.find_element_by_id("fromStationText").clear()
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_id("fromStationText").send_keys("shenzhenbei")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//div[@id='citem_0']").click()

#目的地定为岳阳东
driver.find_element_by_id("toStationText").clear()
driver.find_element_by_id("toStationText").click()
driver.find_element_by_id("toStationText").send_keys("yueyangdong")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//div[@id='citem_0']/span[@class='ralign'][1]").click()

#点击出发日期框框
driver.find_element_by_xpath("//*[@id='train_date']").click()

#选择出发日期
driver.find_element_by_xpath("//div[@class='cal']/div[@class='cal-cm']/div[@class='cell'][30]/div[@class='so']").click()
driver.implicitly_wait(30)

#点击选择高铁
driver.find_element_by_name("cc_type").click()

#点击查询
driver.find_element_by_xpath("//a[@id='query_ticket']").click()


ticket = True
while ticket:
	try:
		print ("123456")
		ticket1 = driver.find_element_by_xpath("//table/tbody[@id='queryLeftTable']/tr[@id='ticket_6i00000G720F']/td[@class='no-br']/a[1]")
		ticket = False
	except Exception as e:
		print ("没有能抢的票，刷新列表继续")

		#点击查询
		driver.find_element_by_xpath("//a[@id='query_ticket']").click()

	else:
		ticket1.click()
		time.sleep(1)
		driver.find_element_by_xpath("//input[@id='username']").clear()
		driver.find_element_by_xpath("//input[@id='username']").send_keys("15623925120")
        # driver.find_element_by_xpath("//input[@id='password']").clear()
		driver.find_element_by_xpath("//input[@id='password']").send_keys("yw15623925120")
		time.sleep(4)
		# driver.find_element_by_xpath("//ul/li[@class='dl  captchaButton leftTicket-login-button-float']/a[@id='loginSubAsyn']").click()

		code = True
		while code:
			try:
				code1 = driver.find_element_by_xpath("//ul/li[@class='dl  captchaButton leftTicket-login-button-float']/a[@id='loginSubAsyn']")
			except Exception as e:
				
				code = False
				print ("验证码输入正确，请选择乘客")
				time.sleep(2)
				# code = False
			else:
				time.sleep(2)
				code1.click()
				print ("验证码输入cuowu ，请选择乘客")
				driver.find_element_by_xpath("//div[@class='item clearfix'][2]/ul[@id='normal_passenger_id']/li[8]/label").click()
				driver.find_element_by_xpath("//a[@id='submitOrder_id']").click()
				# time.sleep(2)
				# driver.find_element_by_xpath("//*[@id='qr_submit_id']").click()
				# print ("抢票成功，请在30分钟内支付")
				# driver.end()

        		

        		