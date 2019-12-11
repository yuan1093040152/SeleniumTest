#coding=utf-8
import threading
from time import sleep,ctime

def sing():
    for i in range(3):
        print(u"正在唱歌...%d"%i)
        sleep(2)

def dance():
    for i in range(3):
        print(u"正在跳舞...%d"%i)
        sleep(2)

def function():
    for x in range(4):
        print (u'哈哈哈...%d'%x)
        sleep(2)
    

if __name__ == '__main__':
    print(u'---开始---:%s'%ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t3 = threading.Thread(target=function)

    t1.start()
    t2.start()
    t3.start()

    sleep(8) # 屏蔽此行代码，试试看，程序是否会立马结束？
    print(u'---结束---:%s'%ctime())