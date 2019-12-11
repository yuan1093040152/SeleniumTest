#coding=utf-8
'''
Created on 2018年3月20日

@author: 唐路
'''
import os,re,urlparse,pickle
from link_crawler_3_1 import *



class DiskCache:
    def __init__(self,chche_dir='G:\Crawler\Links'):
        self.chche_dir = chche_dir
        self.max_length = 250
        
    def url_to_path(self,url):
        components = urlparse.urlsplit(url)
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'
        filename = components.netloc + path + components.query
        filename = re.sub('[^/0-9a-zA-Z\-,.;_]','_',filename)
        filename = '/'.join(segment[:255] for segment in filename.split('/'))
        return os.path.join(self.chche_dir,filename)     #只是返回文件文件路径
    
    def __getitem__(self,url):
        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path,'rb') as fp:
                return pickle.load(fp)        #转化成字典类型方便进行读取
        else:
            raise KeyError(url + ' does not exist')
    
    def __setitem__(self,url,result):
        path = self.url_to_path(url)
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(path,'wb') as fp:
            fp.write(pickle.dumps(result))   #转化成bytes类型以便于储存
            
            
if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache())

        
        
        