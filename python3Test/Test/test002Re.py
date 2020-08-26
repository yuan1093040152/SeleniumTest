#coding=utf-8
import re

a = '原单号12435djkasdhkjas去3442阿斯兰的看介绍'

# 定义查找的类型
pattern = re.compile(r'\d+')    #只匹配数字  以群为单位    ['12435', '3442']
pattern1 = re.compile(r'[^\D+]')  #只匹配数字  以个为单位   ['1', '2', '4', '3', '5', '3', '4', '4', '2']

pattern2 = re.compile(r'\D+')     #匹配除了数字以外的所有字符，以群为单位  ['原单号', 'djkasdhkjas去', '阿斯兰的看介绍']
pattern3 = re.compile(r'[^\d+]')  #匹配除了数字以外的所有字符，以个为单位  ['原', '单', '号', 'd', 'j', '看', '介', '绍']





pattern4 = re.compile(r'[^djkasdhkjas]')    #匹配除了djkasdhkjas字母以外的所有字符  以个为单位  ['原', '1', '2',  '绍']

find_number = pattern4.findall(a)

print(pattern2)


text ='site sea sue sweet see case sse loses'
a = re.findall(r'\bs\S*?e\b',text)    #匹配所有以s开头以e结尾的单词   ['site', 'sue', 'see', 'sse']
b = re.findall(r'\bs.*?e\b',text)    #匹配字符串中所有以s开头到e结尾  ['site', 'sea sue', 'sweet see', 'sse']
print(a)

