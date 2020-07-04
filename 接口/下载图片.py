#coding=utf-8
import requests

IMAGE_URL = 'https://i.leyoujia.com/jjslogin/code.jpg'


def request_download(IMAGE_URL):
	r = requests.get(IMAGE_URL)
	with open('E://test//img2.jpg', 'wb') as f:
		f.write(r.content)  

request_download(IMAGE_URL)