#coding=utf-8

#继承类

#定义一个公共类
class common:
    def aa(self):
        return 'AA'
    def bb(self):
        return 'BB'
    def cc(self):
        return 'CC'

#在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class cat(common):

    def __init__(self,name):
        self.name=name

    def dd(self):
        return '他说：%s'%self.name


#在类后面括号中写入另外一个类名，表示当前类继承另外一个类
class dog(common):

    def __init__(self,name):
        self.name=name

    def ee(self):
        return '他说：%s' % self.name

#实例化对象
a1 = cat('我是谁哦')
#打印对象的方法
print(a1.aa())
#打印继承类的方法
print(a1.dd())

#实例化对象
a2 = dog('你是谁哦')
#打印对象的方法
print(a2.bb())
#打印继承类的方法
print(a2.ee())


