#coding=utf-8
from selenium import webdriver
import time,os

driver = webdriver.Chrome()
url="http://www.baidu.com"
driver.get(url)
driver.maximize_window()
# time.sleep(10)
driver.implicitly_wait(30)
driver.find_element_by_xpath("//*[@id='kw']").send_keys(u'selenium')
driver.find_element_by_id('su').click()
time.sleep(2)
current_handle = driver.current_window_handle
driver.find_element_by_xpath("//*[@id='3']/h3/a").click()
time.sleep(3)
all_handles = driver.window_handles
for handle in all_handles:
    if handle != current_handle:
        driver.switch_to_window(handle)
        break
path = driver.find_element_by_xpath("//a[contains(text(),'软件测试门户')]").text
if path ==u'软件测试门户':
    print '成功'
else:
    print '失败'
driver.quit()


# try:
#     driver.find_element_by_id("kwsss").send_keys("selenium")
#     driver.find_element_by_id("su").click()
# except:
#     driver.get_screenshot_as_file("D:\\Program Files\\error_png.png")
# driver.quit()
