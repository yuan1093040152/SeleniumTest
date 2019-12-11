#coding=utf-8
import re
a='公办 / 其他 / 划片小区43个 / 房源903套'
# b = re.findall(r"房源(.*)套",a)
# b = re.findall(r"房源(.+)套",a)
b = re.findall(r"房源(.+?)套",a)
print (b)
print (b[0])