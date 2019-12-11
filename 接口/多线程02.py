#coding=utf-8
from bs4 import BeautifulSoup
import requests,urllib,time,random,bs4,re,threading
from tqdm import tqdm,trange
from xlutils.copy import copy 
import xlrd,xlwt


url = 'http://www.pptbz.com/pptpic/UploadFiles_6909/201211/2012111719294197.jpg'

def aaa():
	
	try:
		b = random.randint(10000,99999)
		path = 'E:\\test\\'+'test_'+str(b)+'.jpg'
		# path = 'C:\\Users\\admin\\Desktop\\'+str(b)+'.jpg'				
		file = urllib.urlopen(url).read()			
		f = open(path,'wb')
		f.write(file)
		for i in trange(100):
			# time.implicitly_wait(0.01)
			time.sleep(0.01)
			pass
		time.sleep(5)
		f.close()
		
	except :
		pass


if __name__ == "__main__":
    for i in range(50):
        t = threading.Thread(target=aaa)
        t.start() #启动线程，即让线程开始执行