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





def target(q):
    while True:
        msg = q.get()
        for i in range(5):
            print ('running thread-{}:{}'.format(threading.get_ident(), i))
            time.sleep(1)

def pool(workers,queue):
    for n in range(workers):
        t = threading.Thread(target=target, args=(queue,))
        t.daemon = True
        t.start()

queue = Queue()
# 创建一个线程池：并设置线程数为5
pool(5, queue)

for i in range(2):
    queue.put("start")

# 消息都被消费才能结束
queue.join()