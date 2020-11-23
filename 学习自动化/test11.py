# coding=utf-8
import re

str = '【乐有家】感谢选择乐有家，您的验证码是：120948（30分钟有效）'

str1 = re.findall('：(.*)（',str)[0]
print (str1)