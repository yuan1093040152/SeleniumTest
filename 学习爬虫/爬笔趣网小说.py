#coding=utf-8
from bs4 import BeautifulSoup
import requests,time,bs4,re
#解决编码格式无法识别
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

# url = 'http://www.biquku.la/16/16889/'
url = 'http://www.biquku.la/16/16532/'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}  
start_html = requests.get(url,headers=headers) 

demo = start_html.text
# print (demo)

soup = BeautifulSoup(demo,'lxml')
list1 = soup.find('div',id ='list').find_all('a')
# print (list1)

# 获取章节列表地址
# print ('获取章节列表地址')
c = 0
for link in list1:
	try:
		
		c = c+1
		links = link['href']
		# print (links)
		links_all = url+links
		# print (links_all)

		headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
		start_html1 = requests.get(links_all,headers=headers)
		start_html1.encoding = 'utf-8'
		# print (start_html)
		demo1 = start_html1.text
		# print (demo1)

		soup = BeautifulSoup(demo1,'lxml')
		# print (soup)

		# 获取标题
		title = soup.find('div',class_="con_top").get_text()#.strip()

		# print (title)
		title1 = re.findall(u'正文(.*)',title)[0]
		# print (title1)

		# 获取内容
		text = soup.find('div',id="content").get_text()#.strip()
		# print (text)
		
		# 下面这样写可以防止被覆盖
		with open('E:\\test\\3.txt','a') as f:
			#换行符
			f.write('\n'+title1+'\n')
			f.write(text)
			# time.sleep(1)
			print ('正在下载第'+str(c)+'章')
			# print('下载中......')
		f.close()
	except:
		pass
print ('已爬完')

		
