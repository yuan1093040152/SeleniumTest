#coding=utf-8
from bs4 import BeautifulSoup
import requests,urllib,time,random

# 请求地址并获取HTML内容
def request1(all_url):	
	headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}  
	start_html = requests.get(all_url,headers=headers) 
	demo = start_html.text
	return demo

#查找所需要爬取的内容
def getimg(demo):
	soup = BeautifulSoup(demo,'lxml')
	#下面两种写法都可以
	# test2 = soup.find_all('img',{'class':"illustration"})
	test2 = soup.find_all('img',class_='illustration')
	return test2

#获取并下载所爬取的内容
def Save_img(test2):
	a = 1	
	for i in test2:
		time.sleep(0.1)
		img = i['src']
		imgurl = 'http:'+img
		print ('开始获取第%s张图片地址'%a)
		print ('开始保存第%s张图片地址'%a)
		print (imgurl)
		#文件夹和文件名地址（随机数命名）
		b = random.randint(10000,99999)
		path = 'E:\\test\\'+'test_'+str(b)+'.jpg'
		#获取图片地址
		file = urllib.urlopen(imgurl).read()
		#打开文件夹
		f = open(path,'wb')
		#图片保存到文件夹
		f.write(file)
		f.close()
		# urllib.urlretrieve(img,"E:\\test\\%s.jpg"%(a))   python3 的写法
		a = a+1

#主函数
def main():
	y = 1
	#爬取的页数
	for x in range(10):
		all_url = 'https://www.qiushibaike.com/imgrank/page/%s'%y
		demo = request1(all_url)
		test2 = getimg(demo)
		Save_img(test2)
		y = y+1

#调用
if __name__ == '__main__':
	main()