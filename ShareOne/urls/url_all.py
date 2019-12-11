#coding=utf-8
from xlutils.copy import copy
from bs4 import BeautifulSoup
import requests,urllib,time,random,xlrd,xlwt
import threading
from tqdm import tqdm,trange

#
def pages(page):
    a = []
    for i in range(1,page+1):
        url = 'https://shenzhen.leyoujia.com/ysl/index/?n=%s'%i
        a.append(url)
    return a


def url_all():
    b = pages(page)
    urlE = []
    for url in b:
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        start_html = requests.get(url, headers=headers)
        demo = start_html.text
        soup = BeautifulSoup(demo,'lxml')
        test2 = soup.find('div',class_="list-box").find_all('div',class_="img")
        # print (test2)

        for test3 in test2:
            test4 = test3.find_all('a')
            # print (test4)

            for urlA in test4:
                urlB = urlA['href']
                # print (url2)
                urlC = 'https://shenzhen.leyoujia.com'
                urlD = urlC+urlB
                # print (url4)
                urlE.append(urlD)
            # print (url5)
    return urlE


def data():
    a = 0
    urlF = url_all()
    print '待爬取url数量：',len(urlF)
    d = a + 1
    for url in urlF:
        # print (url)
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        start_html = requests.get(url, headers=headers)
        demo = start_html.text
        soup = BeautifulSoup(demo, 'lxml')
        # print (soup)
        time.sleep(1)

        #参考均价(元/㎡)
        average_price = soup.find('div', class_="intro").find_all('em')[1].get_text()
        print (average_price)

        #楼盘名称
        name = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[1].get_text()
        print (name)

        #楼盘地址
        address = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[3].get_text()
        print (address)

        #楼盘别名
        alias = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[5].get_text()
        print (alias)

        #产权
        Property_right = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[8].get_text()
        print (Property_right)

        #开盘时间
        start_time = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[10].get_text()
        print (start_time)

        #入住时间
        Check_time = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[12].get_text()
        print (Check_time)

        #绿化率
        Afforestation_rate = soup.find('div',class_="cont").find('ul',class_="clearfix").find_all('span')[34].get_text()
        print (Afforestation_rate)

        #楼盘介绍
        infos = soup.find('div',class_="cont").find('p',class_="more").get_text().strip()
        print (infos)
        # info = re.findall(ur'【[^【】]+】：[^【】]+', infos)[0]
        # print (info)
        #
        # #栋阁户型
        # Apartment = re.findall(ur'【[^【】]+】：[^【】]+', infos)[1]
        # print (Apartment)
        #
        # #周边配套
        # Matching = re.findall(ur'【[^【】]+】：[^【】]+', infos)[2]
        # print (Matching)
        # 打开想要更改或者添加数据的excel文件
        file = 'C:\\Users\\admin\\Desktop\\fangyuan.xls'
        add_excel1 = xlrd.open_workbook(file, formatting_info=True)

        # 复制文件
        add_excel = copy(add_excel1)

        # 获得第一个sheet的对象
        ws = add_excel.get_sheet(0)
        # 写入数据
        # 第二行第十一列（注：0为第一行/列）

        ws.write(d, 0, name)
        ws.write(d, 1, alias)
        ws.write(d, 2, address)
        ws.write(d, 3, average_price)
        ws.write(d, 4, Property_right)
        ws.write(d, 5, start_time)
        ws.write(d, 6, Check_time)
        ws.write(d, 7, Afforestation_rate)
        ws.write(d, 8, infos)
        ws.write(d, 9, url)
        # 保存
        add_excel.save(file)
        print (u'已写入房源信息：'+str(d))
        d = d+1
        time.sleep(2)
    a = a + 12
        #当前URL



#参考：https://www.cnblogs.com/tina-python/p/5508402.html

# var x = /【[^【】]+】：[^【】]+/ig
# 从‘【’开始，
# ‘[^【】]’集合内不包括这两个符号，
# +  匹配一个或多个
# ‘】：’这两个符号后的内容
#‘[^【】]’不匹配这两个括号内的内容，
# + 匹配一个或多个
#i 不分大小写
#g 全局



def Excel():
    print (u'新建xls文件，并写入字段信息')
    file = 'C:\\Users\\admin\\Desktop\\fangyuan.xls'
    # with open(file,'a') as f:
        # 打开想要更改或者添加数据的excel文件
    old_excel1 = xlrd.open_workbook(file,formatting_info=True)

    # 复制文件
    old_excel = copy(old_excel1)

    # 获得第一个sheet的对象
    ws = old_excel.get_sheet(0)
    # 写入数据
    # 第二行第十一列（注：0为第一行/列）

    ws.write(0, 0, u'楼盘名称')
    ws.write(0, 1, u'楼盘别名')
    ws.write(0, 2, u'楼盘地址')
    ws.write(0, 3, u'参考均价(元/㎡)')
    ws.write(0, 4, u'产权')
    ws.write(0, 5, u'开盘时间')
    ws.write(0, 6, u'入住时间')
    ws.write(0, 7, u'绿化率')
    ws.write(0, 8, u'楼盘介绍')
    ws.write(0, 9, u'链接地址')
    # 保存
    old_excel.save(file)
    return file


if __name__ == "__main__":
    start = time.time()
    Excel()
    page = 2
    data()
    end = time.time()
    print ('runing time :%s S'%(end-start))



