#coding=utf-8

from aip import AipOcr
#第一种方法调用百度API识别
#百度ID KEY
def demo():
    APP_ID = '16947930'
    API_KEY = '0ynD0BGPC6QtrPWs68i4sQO9'
    SECRET_KEY = 'fKsckEf41jUtTDBwFIeHYkhnYyvNaViz'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

#读取图片
def get_file_content(imgPath):
    with open(imgPath, 'rb') as f:
        return f.read()

#调用百度ORC高精度识别验证码
def get_image_code(imgPath):
    image = get_file_content(imgPath)
    client = demo()
    image1 = client.basicAccurate(image)
    # print image1
    print (image1['words_result'][0]['words'])

if __name__ == '__main__':
    imgPath = 'E:\\test\\111.jpg'
    get_image_code(imgPath)






