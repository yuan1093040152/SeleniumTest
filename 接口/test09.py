#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()

# a = {"_smt_uid":"5eeabac5.2b0da922","/community/communityDic/communityDic-detail_guidance":"1"}
b = {"/community/communityDic/communityDic-list_guidance":"1","/hsl/index/house-list_guidance":"1"}
c = {"/hsl/house/house-detail_guidance":"1","_ga":"GA1.1.492950869.1592467069"}
d = {"JSESSIONIDUE":"22FC58E6C8898181C7DCA931A2EC9488","fhListCookies":""}
e = {"SESSION":"NjdjZDViNDctNTg4OS00ODM4LTkwN2YtYjk2MTIxMzBkNDVl","/hsl/index/own-house-list_guidance":"1"}
f = {"JSESSIONID":"DFCB68D2FE1C0A544810BCA7B0D760E3"}



# driver.add_cookie(a)
# driver.add_cookie(b)
# driver.add_cookie(c)
# driver.add_cookie(d)
# driver.add_cookie(e)
# driver.add_cookie(f)


driver.get('http://172.16.22.100/jjslogin/tologin')

cookies = driver.get_cookies()
print(cookies)

driver.close()
driver.quit()
