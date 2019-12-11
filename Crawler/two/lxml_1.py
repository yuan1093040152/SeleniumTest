#coding=utf-8
'''
Created on 2018年3月15日

@author: 唐路
'''

import lxml.html
import lxml.cssselect
from re_grab import download


# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# tree = lxml.html.fromstring(broken_html)
# print tree
# fixed_html = lxml.html.tostring(tree,pretty_print=True)
# print fixed_html


url = 'http://example.webscraping.com/places/default/view/China-47'
html = download(url)
print html
tree = lxml.html.fromstring(html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
td = tree.cssselect('tr#places_national_flag__row > td.w2p_fw > img')
print td
area = td.text_content()
print area


