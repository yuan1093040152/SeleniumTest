#coding=utf-8
from selenium import webdriver
import time,os,csv,random




def login():
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('http://www.51job.com/')
	time.sleep(2)
	return driver
 

def sousuo(driver):
	driver.implicitly_wait(10)
	driver.find_element_by_id('kwdselectid').send_keys(u'测试工程师')
	driver.find_element_by_xpath('//button[contains(text(),"搜索")]').click()
	time.sleep(3)
	elems = driver.find_elements_by_css_selector('a')
	for elem in elems:
		print (elem.text)
		if u'测试工程师' in  elem.text:
			 return 'True'
	return 'False'


def loginone(driver):
	driver.implicitly_wait(20)
	driver.find_element_by_link_text('登录').click()
	driver.find_element_by_id('loginname').clear()
	driver.find_element_by_id('loginname').send_keys(u'13533630193')
	driver.find_element_by_id('password').clear()
	driver.find_element_by_id('password').send_keys(u'yanggai1994')
	driver.find_element_by_id('login_btn').click()
	time.sleep(2)
	try:
		driver.find_element_by_xpath('//a[contains(text(),"杨凯")]')
		return 'True'
	except:
		return 'False'


def writer(CaseName,Boole):
	fo = open('E:\\Python\\PythonReport\\Report.txt','a')
	value = CaseName.decode('gb2312') + ',' + Boole + '\n'
	fo.write(value)
	fo.close()
	return


def PythonShot(driver,CaseName):#截图
	path = 'E:\\Python\\PythonShot\\%s.png'%CaseName
	driver.get_screenshot_as_file(path)
	return 

def Read():
	fo = open('E:\\Python\\PythonRead\\Cae.csv','rb')
	lines = fo.readlines()
	Cases = []
	for line in lines:
		line = line.strip()
		Cases.append(line)
	return Cases



def case():
	Case = Read()
	i = 1

	driver = login()
	Boole = loginone(driver)
	writer(Case[i],Boole)
	if  Boole == 'False':
		driver.Shot(driver,Case[i])
	driver.quit()

	i += 1
	driver = login()
	Boole = sousuo(driver)
	writer(Case[i],Boole)
	if Boole == 'False':
		driver.Shot(driver,Case[i])
	driver.quit()
	return



try:
	os.remove('E:\\Python\\PythonReport\\Report.txt')
except:
	pass
case()














