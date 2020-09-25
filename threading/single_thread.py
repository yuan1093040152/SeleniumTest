# coding=utf-8
import threading, time
from selenium import webdriver
from queue import Queue


lock = threading.Lock()

def login(name):
    # 创建锁


    '''上锁，第一个线程如果申请到锁，会在执行公共数据的过程中持续阻塞后续线程
       即后续第二个或其他线程依次来了发现已经被上锁，只能等待第一个线程释放锁
       当第一个线程将锁释放，后续的线程会进行争抢'''
    # lock.acquire()



    driver = webdriver.Chrome()
    url = "http://www.baidu.com"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id='kw']").send_keys(name)
    driver.find_element_by_id('su').click()
    time.sleep(10)
    driver.quit()

    # lock.release()  # 释放锁



if __name__ == "__main__":

    # threadmax = threading.BoundedSemaphore(2)
    aa = []
    name = ['python', 'java','C++','PHP','selenium']

    for x in range(1):

    # 创建线程并存入数组
        for i in name:
            t = threading.Thread(target=login, args=(i,))
            aa.append(t)


        print('aa=',aa)

        #a.start() 启动所有线程
        for a in aa:
            a.start()


    # a.join()  # 当所有线程执行完才执行主进程
    for a in aa:
        a.join()


print(u'执行完')
