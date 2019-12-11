# encoding: UTF-8
import threading
import time

# event = threading.Event()
# for x in xrange(5):

# def func(x):
#     # 等待事件，进入等待阻塞状态
#     # print '%s 开始' % threading.currentThread().getName()
#     # print '%s 开始22' % threading.currentThread().getName()
    
    	
#    	event.wait()

#     # 收到事件后进入运行状态
#     print '%s锁住' % threading.currentThread().getName()

# t1 = threading.Thread(target=func)
# t2 = threading.Thread(target=func)
# t1.start()
# t2.start()

# time.sleep(2)

# # 发送事件通知
# print '解锁.'
# event.set()




def aaa():
	abc = []
	for x in xrange(3):
		abc.append(x)
		print (x)
	print(abc[-1])
aaa()



# for y in range(2):
#     t = threading.Thread(target=aaa)
#     t.start()
#     time.sleep(1)
# t.join()
# end = time.time()
# print (u'已爬完')


a = [1,2,3,4,5]
