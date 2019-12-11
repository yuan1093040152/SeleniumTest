#coding=utf-8
from bs4 import BeautifulSoup
from wxpy import *
import requests,sys,datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

#爬新闻数据，写入文件
def news(all_url = 'https://news.baidu.com/'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    start_html = requests.get(all_url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo,'lxml')
    news_title = soup.find('div',class_="hotnews").find_all('li')
    # print (news_title)
    #存入列表
    a = []
    for i in news_title:
        url = i.find_all('a')
        for x in url:
            title = x.get_text()
            a.append(title)
            url1 = x['href']
            a.append(url1)
    # print (a)
    #清空文件内容
    try:
        delete()
    except:
        pass
    # 写入标题
    try:
        title1()
    except:
        pass
    #写入信息
    for b in range(8):
        b1 = a[b]
        with open('E:\\test\\news.txt','a') as f:
            f.write(b1+'\n')
        f.close()
    # 写入标题
    try:
        title2()
    except:
        pass
    # 写入信息
    info = Heart(all_url = 'http://www.59xihuan.cn/')
    with open('E:\\test\\news.txt','a') as f:
        f.write(info+'\n')
    f.close()
    # 写入标题
    try:
        title3()
    except:
        pass
    # 写入信息
    info1 = joke(all_url = 'https://www.qiushibaike.com/')
    with open('E:\\test\\news.txt','a') as f:
        f.write(info1)
    f.close()

#清空文件内容
def delete():
    with open('E:\\test\\news.txt','r+') as f:
        read = f.read()
        f.seek(0)
        f.truncate()
    f.close()

#文件写入新闻标题
def title1():
    now_time = datetime.datetime.now()
    with open('E:\\test\\news.txt', 'a') as f:
        f.write(str(now_time)+u'   袁猛   '+'\n')
        f.write(u'国家大事：' + '\n\n')
    f.close()

#文件写入心灵鸡汤标题
def title2():
    with open('E:\\test\\news.txt', 'a') as f:
        f.write('\n'+u'心灵鸡汤：' + '\n\n')

#文件写入笑话标题
def title3():
    with open('E:\\test\\news.txt', 'a') as f:
        f.write('\n'+u'开心一下：' + '\n\n')

#读取文件信息
def txt_info():
     with open('E:\\test\\news.txt','r') as f:
         txt_info1 = f.read()
         # print (txt_info1)
         return txt_info1

#爬取心灵鸡汤
def Heart(all_url = 'http://www.59xihuan.cn/'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    start_html = requests.get(all_url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo,'lxml')
    heart = soup.find('div',class_="post").find('div',class_="mixed1").find('div',class_="pic_text1").get_text().strip()
    # print ('     '+heart)
    return '     '+heart+u'[奋斗][奋斗]'

#爬取笑话
def joke(all_url = 'https://www.qiushibaike.com/'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    start_html = requests.get(all_url, headers=headers)
    demo = start_html.text
    soup = BeautifulSoup(demo, 'lxml')
    info = soup.find('div',class_="recommend-article").find('li',class_="item typs_word").find('div',class_="recmd-right").find('a',class_="recmd-content")
    url = info['href']
    # print (url)
    url4 = 'https://www.qiushibaike.com'
    all_url1 = url4+url
    # print (all_url1)
    start_html = requests.get(all_url1, headers=headers)
    demo1 = start_html.text
    soup1 = BeautifulSoup(demo1, 'lxml')
    info2 = soup1.find('div',class_="word").find('div',class_="content").get_text().strip()
    # print (info2)
    return '     '+info2+u'[捂脸][捂脸]'

#发送微信
def wechat():
    url_info = news(all_url = 'https://news.baidu.com/')
    title_info2 = txt_info()
    print (title_info2)
    bot = Bot(cache_path=True)
    # 注：如果获取不到群聊，请将群聊保存到通讯录
    # group = bot.groups().search(u'动一动妳发财的小手')[0]
    # # print (group)
    # group1 = bot.groups().search(u'尼古拉斯')[0]
    #发送好友
    friend = bot.friends().search('Test-wechat')[0]
    # print (friend)
    friend_info = friend.send(title_info2)
    # friend_info = group.send(title_info2)
    # friend_info = group1.send(title_info2)
    print (u'已发送')


if __name__ == '__main__':
    # news(all_url = 'https://news.baidu.com/')
    # Heart(all_url='http://www.59xihuan.cn/')
    # joke(all_url = 'https://www.qiushibaike.com/')
    wechat()






