#coding=utf-8

a = [8,6,3,1,7,5]
a.sort(reverse=False)   #False=升序，True=降序
print(a)


#冒泡排序
for x in range(len(a)):
    for y in range (0,len(a)-x-1):
        if a[y]>a[y+1]:
            a[y],a[y+1] = a[y+1],a[y]
print(a)