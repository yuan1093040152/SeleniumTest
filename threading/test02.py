from threading import Thread
from selenium import webdriver
from time import sleep,ctime

#测试用例
def test_baidu(browser,search):
    print('start:%s,' %browser)
    print('browser:%s' %browser)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print('参数有误')

    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    lites = {'chrome':'threading','chrome':'python'} #启动浏览器，指定每个浏览器搜索的内容

    threads = []
    files = range(len(lites))
    #创建多线程
    for browser, search in lites.items(): #字典循环
        t = Thread(target=test_baidu, args=(browser,search))
        threads.append(t)
    #启动多线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s' %ctime())