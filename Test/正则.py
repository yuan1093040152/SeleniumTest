#coding=utf-8
import re,json

# a = u'测试abc12,3，de测试'

# #  \d  数字:[0-9]  匹配字符串中的数字并返回一个列表
# b = re.findall(r'\d',a)
# print (b)
# print(b[0])

# #  \D  非数字  匹配字符串中的非数字并返回一个列表
# c = re.findall(r'\D',a)
# print(c)
# print(c[0])

a = u'【基本信息】：东关·乐尚林居，别称叫乐尚林居，坐落于中山园路58号(同乐村西南侧,宗地面积96208㎡,小区绿化率高。【栋阁户型】：小区总共有5栋、总共约有584户，主要户型有：176.67平米的5室2厅、108.35平米的4室2厅、127.01平米的4室2厅、110.86平米的4室2厅。\r\n【周边配套】：附近五公里内购物和出行都很方便。小区1公里范围内在建地铁12号线同乐站。三大公园环绕。收起全文'

b = re.findall(r'【[^【】]+】：[^【】]+', a)[2]
print (b)


c = u'1、某处理中心收到快件差异报告内容为某快件破损严重。查证结果最不可能是(　　)。'

print (c[2:])




# var x = /【[^【】]+】：[^【】]+/ig
# 从‘【’开始，
# ‘[^【】]’集合内不包括这两个符号，
# +  匹配一个或多个
# ‘】：’这两个符号后的内容
#‘[^【】]’不匹配这两个括号内的内容，
# + 匹配一个或多个
#i 不分大小写
#g 全局
