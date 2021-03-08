# coding=utf-8
from bs4 import BeautifulSoup
import requests, time, bs4, re

# python2  解决编码格式无法识别
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# http://www.paoshuzw.com/51/51033/21796672.html
# http://www.paoshuzw.com/51/51033//51/51033/21796672.html

url = 'http://www.paoshuzw.com/51/51033/'
url1 = 'http://www.paoshuzw.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
start_html = requests.get(url, headers=headers)

demo = start_html.text
# print (demo)

soup = BeautifulSoup(demo, 'lxml')
list1 = soup.find('div', id='list').find_all('a')
# print (list1)

# 获取章节列表地址
# print ('获取章节列表地址')
c = 0

for link in list1:
    # try:

    c = c + 1
    # try:

    links = link['href']
    # print (links)
    links_all = url1 + links
    print(links_all)
    time.sleep(2)

    # session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    }
    start_html1 = requests.get(links_all, headers=headers)

    # 解决乱码 （类似éç»äººè¡¨ç®çé¿å å­åè格式的编码）
    start_html1.encoding = start_html1.apparent_encoding

    # print (start_html1)
    demo1 = start_html1.text

    print (demo1)

    soup = BeautifulSoup(demo1, 'lxml')
    # print ('soup=',soup)
    #//*[@id="content"]/text()[1]
    try:
        # # 获取标题
        # title = soup.find('div', class_="con_top").get_text()  # .strip()
        title = soup.find('div', class_="bookname").find_all('h1')[0]#.get_text()

        #去掉字符串内的符号（只留中文）
        title = ''.join(str(title))
        title1 = re.sub("[A-Za-z0-9\>\<\/']", "", title)
        print(title1)
        # title1 = title.get_text()
        # print (type(title))
        # print (title)
        # title1 = re.findall(u'正文(.*)', title)[0]
    except:
        title1='\n该标题没找到\n'
        print(title1)
        pass

    try:

        # 获取内容
        text = soup.find('div', id="content").string#.get_text()#.strip()
        print (text)
    except:
        text = '\n该内容没找到\n'
        print('该内容没找到')
        pass
#
#     # 下面这样写可以防止被覆盖
#     # with open('E:\\test\\3.txt', 'a') as f:
#     # python3 指定编码格式
#     with open('E:\\test\\3.txt', 'a', encoding='utf-8') as f:
#         # 换行符
#         f.write('\n' + title1 + '\n')
#         f.write(text)
#         time.sleep(3)
#         print('正在下载第' + str(c) + '章')
#         # print('下载中......')
#     f.close()
# # except:
# #     print('---------错误--------')
# #     pass
# print('已爬完')
