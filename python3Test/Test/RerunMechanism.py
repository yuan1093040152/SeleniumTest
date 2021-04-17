#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2021/4/8 13:58
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
#重跑机制装饰器

def failrun(n):
    def decorator(func):
        def wrapper(*args,**kw):
            for i in range(n):
                try:
                    r= func(*args,**kw)
                    return r
                except NameError as err:
                    print('用例第'+str(i+1)+'次失败原因:%s'%err)
            raise NameError
        return wrapper
    return decorator


@failrun(n=2)
def test_b():
    a = '1231231231'
    print(b)


    
test_b()