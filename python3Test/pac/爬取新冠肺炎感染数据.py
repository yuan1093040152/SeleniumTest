#coding=utf-8
import requests,sys,smtplib,urllib3,json,time,pymysql,argparse
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
urllib3.disable_warnings()
# import sys
# reload(sys)
# sys.setdefaultencoding( "utf-8" )


def city_url(url):
    headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    #verify=False 解决报SSL错误
    start_html = requests.get(url,headers=headers,verify=False)
    demo = start_html.text
    # print (demo)
    soup = BeautifulSoup(demo,'lxml')
    lists = str((soup.find_all('script',id='captain-config'))[0])
    print ('---------------------------------------------')
    # print (lists)
    index = lists[52:-9]
    index2 = json.loads(index)
    index3 = index2['component'][0]
    return index3

def Domestic_epidemic():
    soup = city_url(url)
    index3 = soup['caseList']
    # print(len(index3))
    # print(index3)
    print('疫情最新数据时间：  ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for i in range(len(index3)-1,-1,-1):
        region = (index3[i])
        #疫情地区
        city =region['area']
        #今日新增
        new_add = region['confirmedRelative']
        #现有病例
        Existing = region['curConfirm']
        #累计病例
        Cumulative = region['confirmed']
        #治愈病例
        Cure = region['crued']
        #死亡病例
        death = region['died']
        print('疫情地区:%s      今日新增:%s 人      现有病例:%s 人      累计病例:%s 人      治愈病例:%s 人      死亡病例:%s 人'%(city,new_add,Existing,Cumulative,Cure,death))



def Epidemic_situation_abroad():
    soup = city_url(url)
    index3 = soup['caseOutsideList']
    # print(len(index3))
    # print(index3)
    print('疫情最新数据时间：  ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+ '\n')
    #倒序遍历
    for i in range(len(index3)-1,-1,-1):
        region = (index3[i])
        #疫情地区
        city =region['area']
        #今日新增
        new_add = region['confirmedRelative']
        #现有病例
        Existing = region['curConfirm']
        #累计病例
        Cumulative = region['confirmed']
        #治愈病例
        Cure = region['crued']
        #死亡病例
        death = region['died']
        print('疫情地区:%s      今日新增:%s 人      现有病例:%s 人      累计病例:%s 人      治愈病例:%s 人      死亡病例:%s 人'%(city,new_add,Existing,Cumulative,Cure,death))

if __name__ == '__main__':
    url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3#tab4'


    parser = argparse.ArgumentParser()
    parser.add_argument("SelectArea")
    args = parser.parse_args()
    param = vars(args)
    SelectArea = param['SelectArea']
    print ('地区为：',SelectArea)

    if SelectArea == 'China':
        #国内
        Domestic_epidemic()

    elif SelectArea == 'No_China':
        #国外
        Epidemic_situation_abroad()

    else:
        print('查询失败')



