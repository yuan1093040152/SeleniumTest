#coding=utf-8
'''
Created on 2018年7月18日

@author: Administrator
'''
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException



def get_page_detail():
    try:
        data = {'start': 10000,'end': 18082}
        url = 'http://datachart.500.com/ssq/history/newinc/history.php?' + urlencode(data)
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None
    

def parse_page_index(html):
    print (html)
    soup = BeautifulSoup(html,'lxml')
#     title = soup.head.title.string
#     print (title)
    items = soup.select('#tdata .t_tr1')
    for item in items:
        tr = item.select('td')
        trlist = []
        i = 0
        for td in tr:
            i += 1
            if i == 9:
                trlist.append('0')
                continue
            trlist.append(td.get_text())
            
        print (trlist)
        wirte_csv(trlist)
         
        


import csv
def wirte_csv(list):
    csvFile=open("F:\\Crawler\\Csv\\caipiao.csv",'a',newline='')
    writer=csv.writer(csvFile)
    writer.writerow(list)
    csvFile.close()


        
def writr(list):
    with open('F:\\Crawler\\Csv\\caipiao.csv','a',newline='') as datacsv:
        csvwriter = csv.writer(datacsv,dialect = ("excel"))
        csvwriter.writerow(list)
    datacsv.close()


def main():
    html = get_page_detail()
    parse_page_index(html)
    
    
if __name__ == '__main__':
    main()