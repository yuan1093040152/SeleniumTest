#coding=utf-8
import time,datetime

def timec():
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    print (nowtime)
    return nowtime

def file():
    for i in range(10):
        nowtime = timec()
        time.sleep(1)
        with open('E:\\test\\'+str(nowtime)+'666.txt','a+') as f:
            f.write('hello world')
            f.close()
        print(f)

if __name__ == '__main__':
    timec()