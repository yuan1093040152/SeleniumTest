#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
from pyquery import PyQuery as pq


html = '''
<div id="container">
    <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">socood item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth ttem</a></li>
    </ul>
</dlv>
'''
# doc = pq(url='http://www.baidu.com')
# print (doc('head'))

doc = pq(html)
# print (doc)
# print (doc('li'))
# print (doc('#container .list li'))
items = doc('.list')
print (type(items))
print (items)
lis = items.find('li')
print (lis)


lis = items.children()
print (lis)


lis = items.children('.active')
print (lis)


container = items.parent()
print (container)

container = items.parents()
print (container)


lis = doc('li').items()
for li in lis:
    print (li)

a = doc('.item-0.active a')
print (a)
print (a.attr('href'))
print (a.attr.href)
print (type(a.attr.href))

li = doc('.item-0.active')
print (li.html())


print (li)
li.removeClass('active')
print (li)

li.addClass('active')
print (li)

li.attr('name','link')
print (li)

li.css('font-size','14px')
print (li)

li.find('span').remove()
print (li)














