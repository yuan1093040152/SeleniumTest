#coding=utf-8

#实例化对象

#定义一个类
class testname:

    #定义公共的属性
    aa = '123'

    #定义私有的属性,私有属性在类外部无法直接进行访问
    _sex = '234'

    #可以用来为每个实例定制自己的特征
    def __init__(self,name,arg,sex):
        #定义一个昵称： self.对象的属性1 = 参数1
        self.name = name
        self.arg = arg
        self.sex = sex

    #定义公共的方法
    def info(self):
        return 'woca'

    def testinfo(self,info):
        return info+'我叫%s，今年%d，性别%s'%(self.name,self.arg,self.sex)

#打印公共的属性
print(testname.aa)
#引用方法
print(testname.info)

#实例化对象并调用__init__方法 （‘类名+括号’），参数与init对应，不需要传self
p = testname('小明',18,'男')

#打印对象的属性
print(p.name)
#打印对象的方法
print(p.info())
print(p.testinfo('333333'))