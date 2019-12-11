
#coding=utf-8
import T_006
# from T_006 import cc


def bubble_sort(lists):   #冒泡排序
    len_list=len(lists)
    for i in range(len_list):
        for j in range(len_list-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1]=lists[j+1],lists[j]
        print(lists)
    return lists



def insert_sort(lists):      #插入排序

    for i in range(len(lists)):
        position=i

        while position>0:
            if lists[position]<lists[position-1]:
                lists[position],lists[position-1]=lists[position-1],lists[position]
            position-=1
        print(lists)
    return lists



# cc()
# T_006.cc()

# a = '   kfsdl   sdlk   '

# print (a.replace('sdl','sss'))  #换字
# print (a.replace('l   ','d'))   #去中间的空格

# print (a.strip())     #去头尾的空格
# print (a.strip().strip('k'))  #去头尾的字


