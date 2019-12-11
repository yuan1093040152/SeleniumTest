#coding=utf-8

from PIL import Image
import pytesseract

def demo(imgpath):
    image = Image.open(imgpath)
    code = pytesseract.image_to_string(image,lang="eng",config="-psm 7")
    return code


if __name__ == '__main__':
    imgpath ='D:\\Program Files\\SeleniumTest\\CodeDemo\\1.jpg'
    Img = demo(imgpath)
    print Img
