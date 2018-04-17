'''
__name__  
模块就是一个可执行的py文件
不想让模块里的某些代码执行 可以用__name__ 调用程序中的一部分
每一个模块都有__name__属性
'''

if __name__ == "__main__":
    print("自身调用")
else:
    print(__name__)
    '''
    模块 类 面向对象
    一个py文件就是一个类
    封装函数 复用,维护性高
    '''
    def custom_sum():
        print(1 + 1)