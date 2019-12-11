#coding=utf-8
from selenium import webdriver
import time,os
import win32api
 
#获取当前屏幕分辨率
def get_Screen():
	aa = []
	driver = webdriver.Chrome()
	# driver.maximize_window() 
	# driver.get('https://www.baidu.com')
	js = 'var winW = window.screen.width;var winH = window.screen.height;alert(winW+","+winH)'
	driver.execute_script(js)
	# a='E:\\test\\11.png'
	line = driver.switch_to_alert().text
	driver.switch_to_alert().accept()
	size = line.split(',')
	# print (size)
	# Screen = {}
	# Screen['width'] = int(size[0])
	# Screen['height'] = int(size[1])
	# time.sleep(3)
	# driver.quit()
	driver.close()
	width = int(size[0])
	aa.append(width)
	height = int(size[1])
	aa.append(height)
	print (aa)
	return aa

	# return Screen
def  win32():
	
	dm = win32api.EnumDisplaySettings(None, 0)
	dm.PelsWidth = 1440
	dm.PelsHeight = 900
	dm.BitsPerPel = 32
	dm.DisplayFixedOutput = 0     #(将值设为1，或者0，在我机器上都为拉伸)
	win32api.ChangeDisplaySettings(dm, 0)


def ResolvingPower():
	Screen = get_Screen()
	print (Screen)
	if Screen[0] == '1440' and Screen[1] == '900':
		pass
	else:
		win32()


if __name__ == '__main__':
 	

	ResolvingPower = ResolvingPower()





