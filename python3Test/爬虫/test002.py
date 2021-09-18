#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/9/9 16:54
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

# 水平向右自动模拟移动滑块
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver = Chrome()
WebDriverWait(driver, 3)
# 隐式等待
# driver.implicitly_wait(10)
try:
    driver.maximize_window()
    url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    driver.get(url)
    sleep(3)
    # 切换iframe
    driver.switch_to.frame('iframeResult')
    # 目标位置
    target = driver.find_element_by_id('droppable')
    # 原位置
    source = driver.find_element_by_id('draggable')

    # 方法一移动滑块，此方法一瞬间移动过去，不建议使用
    # action = ActionChains(driver)  # 拿到动作链对象
    # action.drag_and_drop(source,target)
    # action.perform()

    # 方法二：按照偏移量进行移动，此刻移动滑块是水平向右移动
    ActionChains(driver).click_and_hold(source).perform()

    # 偏移量的计算是目标位置x轴的值减去要移动的滑块的x轴的值

    a = target.location['x']
    print(a)
    b = source.location['x']
    print(b)
    distance = a - b
    i = 0
    # 模拟缓慢的滑动
    while i <= distance:
        sleep(0.1)
        ActionChains(driver).move_by_offset(15, 0).perform()
        i += 15
    # 释放鼠标
    ActionChains(driver).release().perform()
    sleep(0.5)
    # 有个弹窗,点击确定
    driver.switch_to.alert.accept()

finally:
    sleep(5)
    driver.close()
