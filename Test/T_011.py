#coding=utf-8
from bs4 import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> ,
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""


# 创建 beautifulsoup 对象
soup = BeautifulSoup(html,'lxml')

#查询网页结构树中第一个符合条件的元素
Find = soup.find('a')
print(Find)

#查询网页结构树中所有符合条件的元素并返回一个列表
find_all = soup.find_all('a')
print (find_all)

#正则匹配a标签下该链接所包含的所有元素
Z = soup.find_all('a',href=re.compile(r'tillie'))
print (Z)

# 组合查询
X = soup.find('p',class_="story").find_all('a',id="link2")
print (X)



# soup = BeautifulSoup(html,"lxml")  #第一个参数指定文本内容，第二个参数解析器
# print(soup.prettify())  #容错性的体现，自动补全
# print(soup.a)  #只找到了一个，而且是从整个文档树找
# print(soup.a.text)   #找到a标签里面的文本
# print(soup.text)   #找整个文档树种所有的文本
# print(soup.a.attrs)   #找a标签的所有属性，字典形式
# print(soup.a.attrs["href"])  #找a标签的href属性
# print(soup.p.b)  #嵌套查找，这是只找一个
# print(soup.p.contents)  #子节点，找到的是一个闭标签
# print(list(soup.p.children )) #得到生成器
# print(list(soup.p.descendants))  #所有的子子孙孙
# print(soup.a.parent)#找父亲
# print(list(soup.a.parent))#父亲的父亲的父亲
# print(soup.p.find_all() ) #标签名可以和find可以结合在一起使用