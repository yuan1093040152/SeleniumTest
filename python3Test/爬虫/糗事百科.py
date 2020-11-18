#coding=utf-8
import requests,sys,smtplib
from bs4 import BeautifulSoup

sys.setrecursionlimit(3000)  # 将默认的递归深度修改为3000

def link_list(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    start_html = requests.get(url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo, 'lxml')
    # print(soup)

    link_all = soup.find_all('a',class_='contentHerf')
    # print(link_all)

    inurl = 'https://www.qiushibaike.com'
    for link in link_all:
        src = inurl+link['href']
        print(src)

        start_html_1 = requests.get(src, headers=headers)
        demo = start_html_1.text
        soup1 = BeautifulSoup(demo, 'lxml')
        # print(soup1)

        try:
            title = soup1.find('div',class_="content").get_text()
            print(title)
        except:
            pass

        try:
            shenping = soup1.find('div',class_="comment-title").get_text()
            print(shenping)
        except:
            pass
        for i in range (5):
            sp = soup1.find('div',class_="comments").select_one('div.comments-list.clearfix')

            sp_name = sp.find('a', class_="userlogin").get_text()
            sp_info = sp.find('span', class_="body").get_text()
            print(sp_name+':'+sp_info)




        # try:
        #     sp_name = soup1.find_all('a', class_="userlogin")
        #     for sp_name1 in sp_name:
        #         sp_name2 = sp_name1.get_text()
        #         print(sp_name2)
        # except:
        #     pass
        #
        # try:
        #     sp_info = soup1.find_all('span', class_="body")
        #     for sp_info1 in sp_info:
        #         sp_info2 = sp_info1.get_text()
        #         print(sp_info)
        # except:
        #     pass













if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/text/'

    link_list(url)