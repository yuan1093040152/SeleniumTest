#coding=utf-8
'''
Created on 2018年3月13日

@author: 唐路
'''
import re,time,csv

def times():
    now_time = int(time.time())
    localtime = time.localtime(now_time)
    strftime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
    return strftime

def write(html):
    html = re.sub('><','>\n<',html)
    fo = open('G:\\Crawler\\log\\one.log','w')
    fo.write(html)
    fo.close()
    return




def write_a(html):
    html = re.sub('><','>\n<',html)
    fo = open('G:\\Crawler\\log\\link.log','a')
    current_time = times()
    fo.write(current_time)
    fo.write('\n')
    fo.write(html)
    fo.write('\n\n\n\n\n\n\n\n')
    return


def write_csv(links):
    fo = file('G:\\Crawler\\Crawler_Csv\\countries.csv','ab')
    writer = csv.writer(fo)
    writer.writerow(links)
    fo.close()
    return