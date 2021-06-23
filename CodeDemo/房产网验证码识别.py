#coding=utf-8
# import Image
import ImageEnhance
import os
import urllib
import ImageFilter
import sys
from pytesseract import *
import time


def verfiy_Identification():
#������֤��
  for num in range(10): 
    url = 'http://i.jjshome.com/jjslogin/code'
    file = ("./Initial/"+str(num)+".bmp","wb").write(urllib.urlopen(url).read())

# ��ֵ��
threshold = 50
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#����ʶ�����ĸ�� ���øñ��������
##rep={'O':'0',
##  'L':'1',
##  'Z':'2',
##  'S':'3',
##  '9':'g'
##  };

def  getverify1(num):
    
    #��ͼƬ
    im = Image.open("./Initial/"+str(num)+".bmp")

    #ת��������
    imgry = im.convert('L')

    #��ֵ��
    out = imgry.point(table,'1')

    #ʶ��
    text = image_to_string(out)
    time.sleep(1)
    #ʶ�����
    text = text.strip()
    text = text.upper();

##    for r in rep:
##        text = text.replace(r,rep[r])


    print text
    return text


if __name__=="__main__":
    verfiy_Identification()
    for num in range(10): 
      getverify1(num)
  
