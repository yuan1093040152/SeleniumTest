#coding=utf-8
#注意python3  print需要加括号
import threading,queue,time
from queue import Queue

#先进先出
# q = queue.Queue()         #定义先进先出
# for i in range(5):        #循环存入队列
#     q.put(i)
# while not q.empty():      #判断队列是否为空
#     print (q.get())       #循环消费
#
# #后进先出
# q = queue.LifoQueue()     #定义后进先出
# for i in range(5):        #循环存入队列
#     q.put(i)
# while not q.empty():      #判断队列是否为空
#     print (q.get())       #循环消费



def pool(workers,queue):
    for n in range(workers):
        t = threading.Thread(target=target, args=(queue,))
        t.daemon = True    # 设置线程是否随主线程退出而退出，默认为False
        t.start()


def target(a):
    # while True:
    msg = a.get()      #循环消费
    for i in range(3):
        print (str(msg)+'\n')
        time.sleep(1)
    # for i in range(5):
    #     print ('running thread-{}:{}'.format(msg,i))
    #     time.sleep(1)



#创建队列-先进先出
queue = queue.Queue()


for i in range(10):
    queue.put(i)    #循环存入队列


# 创建一个线程池：并设置线程数为5
pool(5,queue)



# 消息都被消费才能结束
queue.join()


#创建5个线程来读取queue存入的10个数，并消费3遍



