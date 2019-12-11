#coding=utf-8
'''
Created on 2018年7月15日

@author: kai.yangf
'''
import re

content = 'Hello 1234567 World_This is a Regex_Demo'
result = re.match('He.*?(\d+).*Demo$',content)
print (result)
print (result.group(1))



content = '''Hello 1234567 World_This 
is a Regex_Demo'''
result = re.match('He.*?(\d+).*Demo$',content,re.S)
print (result)
print (result.group(1))
 

content = 'price is $5.00'
result = re.match('price is \$5\.00',content)
print (result)







content = 'Extra stings Hello 1234567 World_This is a Regex_Demo Extra stings'



result = re.search('e.*?(\d+).*Demo',content)
print (result)
print (result.group(1))


content = 'Extra stings Hello 1234567 World_This is a Regex_Demo Extra stings'

content = re.sub('\d+',r' 548',content )

print (content)











