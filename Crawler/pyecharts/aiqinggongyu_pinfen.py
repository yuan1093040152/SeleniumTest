#coding=utf-8
from pyecharts import Bar, Scatter3D
from pyecharts import Page

scorelist = []
with open('爱情公寓_new.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        try:
            line = line.strip()
            value = line.split(',')
            if '-' in value[2]:
                continue
            try:
                float(value[2])
            except ValueError:
                continue
            scorelist.append(float(value[2]))
        except IndexError:
            pass
area_index = list(set(scorelist))
print (area_index)
area_index.reverse()
print (area_index)
area_count = []
for index in area_index:
    area_count.append(scorelist.count(index))
print (area_count)


       # step 1


bar = Bar("猫眼评分不完全数据统计")
bar.add("评分", area_index, area_count, is_stack=True)
       # step 2
 
 
 
 
bar.render()        # step 3