'''
装饰器:
是一个闭包,把一个函数当做参数返回一个替代版的函数,本质上就是一个返回函数的函数
'''

#简单的装饰器
def func1():
    print("wwwwwws")

def func2(func):
    def func3():
        print("*******")
        func()
    return func3()

f = func2(func1)

# __author__ = 'Michael Liao'
# print(__author__)

#复杂的装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("???")

now()