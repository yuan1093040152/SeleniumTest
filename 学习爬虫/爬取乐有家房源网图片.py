#coding=utf-8
from bs4 import BeautifulSoup
import requests,urllib,time,random,re
import threading
from tqdm import tqdm,trange

def function11(all_url):
	headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}  
	                         
	start_html = requests.get(all_url,headers=headers) 
	demo = start_html.text
	soup = BeautifulSoup(demo,'lxml')
	test2 = soup.find('div',class_='list-box').find_all('img',class_="lazy")
	return test2

def main():
	a = function11(all_url)
	print (a)
	# for i in a:
	# 	img = i['data-original']
	# 	print (img)
	# 	img1 = re.findall(r"(.*)/w/200/h/150",img)[0]
	# 	print (img1)
	# 	# return img1


# def downlord():
# 	b = main()
# 	print (b)
# 		# print (u'正在下载：',img1)
# 		c = random.randint(10000,99999)
# 		path = 'E:\\test\\'+'test_'+str(c)+'.jpg'
# 		file = urllib.urlopen(img1).read()
# 		f = open(path,'wb')
# 		f.write(file)
# 		# for i in trange(100):
# 		# 	time.sleep(0.01)
# 		f.close()

			
if __name__ == "__main__":
	for y in range(1,3):
		all_url = 'https://shenzhen.leyoujia.com/ysl/index/?n=%s'%y
		print (all_url)
	# 	# downlord()
		main()
	#
	# for s in range(2):
	# 	t = threading.Thread(target=main)
	# 	# threads.append(t)
	# 	t.start() #启动线程，即让线程开始执行
	# 	time.sleep(2)
	#


