#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2020/12/21 9:46
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from aip import AipOcr
import os


def GetImageCode():
    APP_ID = '16947930'
    API_KEY = '0ynD0BGPC6QtrPWs68i4sQO9'
    SECRET_KEY = 'fKsckEf41jUtTDBwFIeHYkhnYyvNaViz'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open('E://test//FKHD.png', 'rb') as f:
        image = f.read()

    image1 = client.basicAccurate(image)

    #高精度带参数
    # options = {}
    # options["recognize_granularity"] = "big"
    # options["language_type"] = "CHN_ENG"
    # options["detect_direction"] = "true"
    # options["detect_language"] = "true"
    # options["vertexes_location"] = "true"
    # options["probability"] = "true"
    #image1 = client.basicAccurate(image, options)


    # print(image1)
    # print (image1['words_result'][0]['words'])
    # return image1['words_result'][0]['words']
    a =[9,10,17,18,19]

    for i in a:
        print(image1['words_result'][i]['words'])




GetImageCode()


#获取文件夹下的所有文件
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

file_name('E://test')

