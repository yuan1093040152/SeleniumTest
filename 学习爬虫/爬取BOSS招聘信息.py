
#coding=utf-8

from bs4 import BeautifulSoup
import requests,urllib,time,random,bs4,re,sys
from xlutils.copy import copy
import xlrd,xlwt



def Reptilian(test,page):
	a = 0
	for x in range(1,page):

		url = 'https://www.zhipin.com/c101280600/?query='+test+'&page=%s&ka=page-2'%x

		print (u'正在爬取第'+str(x)+u'页：')+url

		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
		start_html = requests.get(url,headers=headers)
		start_html.encoding = 'UTF-8'
		demo = start_html.text
		print ('11111111111111111111111111111111')
		print (type(demo))
		print (demo)
		soup = BeautifulSoup(demo,'lxml')
		print ('33333333333333333333333333333')
		print (soup)
		test1 = soup.find_all('a',href=re.compile(r'/job_detail(.*).html'))
		print ('22222222222222222222222222')
		print (test1)
		d =a + 1
		for link in test1:
			time.sleep(5)
			links = link['href']
			links1 = 'https://www.zhipin.com'
			link_all = links1+links
			print (link_all)

			headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
			start_html = requests.get(link_all,headers=headers)
			demo = start_html.text
			# print (demo)

			soup = BeautifulSoup(demo,'lxml')
			# 获取公司简称
			test01 = soup.find('h3',class_="name")
			test02 = test01.get_text()
			# print (test02)

			# 获取公司全称
			test03 = soup.find('div',class_="detail-content").find('div',class_="name")
			test04 = test03.get_text()
			# print (test04)

			# 获取应聘岗位
			test05 = ((soup.find('div',class_="info-primary").find_all('h1'))[0])
			test06 = test05.get_text()
			# print (test06)

			# 获取薪资待遇    (value = value.srtip()去空格)
			test07 = soup.find('div',class_="info-primary").find('span',class_="badge")
			test08 = test07.get_text().strip()
			# print (test08)

			# 获取任职要求
			test09 = soup.find('div',class_="info-primary").find('p')
			test10 = test09.get_text()
			# print (test10)

			# 获取公司产品
			test11 = soup.find('div',class_="info-company").find('p')
			test12 = test11.get_text()
			# print (test12)

			# 获取岗位职责
			test13 = (soup.find('div',class_="text")).get_text().strip()
			# print (type(test13))
			# test14 = re.findall(r"岗位职责>(.*)<任职资格",test13)
			# print (test13)

			# 获取任职资格

			# 获取工作地址
			test15 = soup.find('div',class_="location-address")
			test16 = test15.get_text()
			# print (test16)

			# 定义文件地址
			file = 'C:\\Users\\admin\\Desktop\\bosszhaopin.xls'

			# 打开想要更改或者添加数据的excel文件
			old_excel1 = xlrd.open_workbook(file, formatting_info=True)

			# 复制文件
			old_excel = copy(old_excel1)

			# 获得第一个sheet的对象
			ws = old_excel.get_sheet(0)
			# 写入数据
			# 第二行第十一列（注：0为第一行/列）

			ws.write(d, 0, test02)
			ws.write(d, 1, test04)
			ws.write(d, 2, test06)
			ws.write(d, 3, test08)
			ws.write(d, 4, test10)
			ws.write(d, 5, test12)
			ws.write(d, 6, test13)
			ws.write(d, 7, test16)
			ws.write(d, 8, link_all)
			# 保存
			old_excel.save(file)
			d = d+1
		a  = a+30

def main():
	try:
		a = 0
		test = u'自动化测试' #输入要爬取的岗位
		page = 2               #输入爬取的页数
		Reptilian(test,page)
	except :
		pass

if __name__ == '__main__':
	main()


