#coding=utf-8
import unittest, time, os, multiprocessing
#import commands
from email.mime.text import MIMEText
import HTMLTestRunner
import sys

#指定搜索路径
path = sys.path.append('\\threading')



def EEEcreatsuite1():

    '''定义casedir列表，读取 threading 目录下的文件/文件夹，找到文件/文件夹的名包含
“thread”的文件/文件夹添加到 casedir 列表中（即 thread_test1 和 thread_test2 两个文件夹）'''

    casedir=[]
    listaa=os.listdir(path)
    for xx in listaa:
        if "thread" in xx:
            casedir.append(xx)
    print (casedir)


    '''定义suite列表，for 循环读取 casedir 数组中的数据（即 thread_test1 和 thread_test2 两个文件夹）。
通过 discover 分别读取文件夹下匹配 start_*.py 规则的用例文件，将所有用例文件添加到
testunit 测试条件中，再将测试套件追加到定义的 suite 数组中。
在整个 EEEcreatsuite1()函数中 返回 suite 和 casedir 两个数组的值。'''

    suite=[]
    for n in casedir:
        testunit=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(str(n),pattern='start_*.py',top_level_dir=r'E:\\test')
        print('discover=',discover)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print (testunit)
        suite.append(testunit)
    print('suite=',suite)
    # return suite,casedir



def EEEEEmultiRunCase(suite,casedir):

    '''定义 proclist()函数，for 循环把 suite 数组中的用例执行结果写入 HTMLTestRunner 测试报
告。multiprocessing.Process 创建用例执行的多进程，把创建的多进程追加到 proclist 数组中，
for 循环 proc.start()开始进程活动，proc.join()等待线程终止。'''

    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
    filename = 'E:\\test\\'+now+'result.html'
    # fp = file(filename, 'wb')
    proclist = []
    s = 0
    fp = open(filename,'wb')

    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况：' )

    proc = multiprocessing.Process(target=runner.run,args=(i,))
    proclist.append(proc)
    s=s+1
    for proc in proclist:
        proc.start()

    for proc in proclist:
        proc.join()
    fp.close()
if __name__ == "__main__":
    runtmp=EEEcreatsuite1()
    # EEEEEmultiRunCase(runtmp[0],runtmp[1])



