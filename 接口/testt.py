from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://i.leyoujia.com/jjslogin/tologin")
driver.implicitly_wait(15)

driver.find_element_by_id('workerStr').clear()
driver.find_element_by_id('workerStr').send_keys('袁猛')

driver.find_element_by_xpath('//a[@class="ui-corner-all"]').click()