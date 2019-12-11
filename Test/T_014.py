# -*- coding: UTF-8 -*-
from selenium import webdriver
import time

 
# class Employee:
#    '所有员工的基类'
#    empCount = 0
 
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount
 
#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary
 
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount 


class login:
   url = 'https://www.baidu.com'
   """docstring for login"""
   # def __init__(self):
   #    self.url = url
   #    super(login, self).__init__()
   #    self.arg = arg

   def login1(self):
      # url = 'https://www.baidu.com'
      self.driver = webdriver.Chrome()
      self.driver.get(self.url)
      time.sleep(1)
      self.driver.quit()

t = login()
t.login1()
