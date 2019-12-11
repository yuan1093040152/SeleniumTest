# coding=utf-8


from baike_spider import url_manager,html_downloader,html_parser,html_outputer
from bs4 import BeautifulSoup
import re
import urllib2
import urlparse

url ='https://baike.baidu.com/item/Python/407313'

# 词条URL格式：/item/XXX

#标题：   <dd class="lemmaWgt-lemmaTitle-title">

#简介：<div class="lemma-summary" label-module="lemmaSummary">

#URL管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #想管理器中添加一个新的URL
    def add_new_url(self,url):
        #判断
        if url is None:
            return
        #如果这个URL既不在新的URL列表里面也不在爬取过的URL列表里面
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)




    # 想管理器中添加批量的URL
    def add_new_urls(self,urls):
        #如果列表为空，不进行添加
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            #单个添加
            self.add_new_url(url)

    #判断管理器中是否有新的待爬取的URL
    @property
    def has_new_url(self):
        #如果列表长度不为0，有待爬取的URL
        return len(self.new_urls) != 0


    #从管理器中获取一个新的待爬取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url




#URL下载器
class UrlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()




#HTML解析器
class HtmlParser(object):

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"item"))
        for link in links:
            new_url = link['self']
            #两个URL拼接成一个完整的url
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}
        type(res_data)


        #url
        res_data['url'] = page_url
        ##标题：   <dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # 简介：<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text ()

        return res_data





#数据写入HTML页面中
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    #收集数据
    def collect_data(self,data):
        if data is None:
            self.datas.append(data)



    def output_html(self):
        fout = open('output.html','w')

        fout.write('<html>')
        fout.write ('<body>')
        fout.write ('<table>')

        for data in self.datas:
            fout.write ('<tr>')
            fout.write ('<td>%s</td>' % data['url'])
            fout.write ('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write ('<td>%s</td>' % data['summary'].encode('utf-8'))

            fout.write ('</tr>')


        fout.write ('</table>')
        fout.write ('</body>')
        fout.write ('</html>')

        fout.close()






#编写main函数

class SpiderMain(object):
    #初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = url_downloader.UrlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self,root_url):
        count = 1
        #将URL添加进待爬取得URL中
        self.urls.add_new_url(root_url)
        #启动爬虫循环
        while self.urls.has_new_url:
            try:
                #获取一个新的URL
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' %(count,new_url))
                #启动下载器下载页面
                html_cont = self.downloader.download(new_url)
                #调用解析器解析页面,得到新的URL列表和新的URL数据
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                #得到的新的URL和数据添加进URL管理器
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count==1000:
                    break
                count = count +1
            except:
                print ('该页面无数据')

        #调用HTML页面输出数据
        self.outputer.output_html()




if __name__=="__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    #启动爬虫
    obj_spider.craw(root_url)

