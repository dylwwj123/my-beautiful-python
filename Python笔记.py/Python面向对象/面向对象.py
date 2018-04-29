'''
面向过程：
自上而下顺序执行。
程序流程写程序时已经确定。

面向对象：
把数据及对数据的操作方法放在一起，作为一个相互依赖的整体。
程序流程由用户在使用中决定。

类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
实例变量：定义在方法中的变量，只作用于当前实例的类。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。
     例如，有这样一个设计：一个Dog类型的对象派生自Animal类，素以Dog也是一个Animal。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
'''

# object:基类 所有类的父类,一般没有合适的就写object
class Person1(object):

    # 定义属性(变量)
    # name = "??"
    # age = 10
    # height = 10

    #定义方法(函数)
    #方法的参数 self必须当第一个参数
    #self代表类的实例
    def level(self):
        print("6年级")
    def eat(self,foot):
        print("在吃",foot)
    def say(self):
        pass
        print("%s-%d-%d" %(self.name,self.age,self.height))
    def cry(jb):
        pass
        print(jb.name)

  # 构造函数 __init__() 在使用类创建对象的时候自动调用,不写默认添加一个空的构造函数
    # self代表类的实例，而非类，哪个对象调用方法，那么该方法中的self就代表那个对象
    # self.__class__ 代表类名
    def __init__(self,name,age,height,money):
        self.name = name
        self.age = age
        self.height = height
        self.__money = money


    #通过内部的方法修改私有属性
    def setMoney(self,intm):
        self.__money = intm

    def getMoney(self):
        return self.__money

    # 重写将函数重新写一遍
    # 描述对象的方法
    # __repr__ 在终端用的 没str 有repr  都有 str = repr
    def __str__(self):
        return "%s,%d,%d" %(self.name, self.age, self.height)

#实例化对象
#实例化两个人,类型相同,内存地址不同
per1 = Person1("tony1",12,180,0)
per1.say()
per1.cry()

per2 = Person1("tony2",16,120,0)
print(per2.name, per2.age, per2.height)

#重写 将函数重新写一遍
per3 = Person1("tony3",3,3,0)
print(per3)

#防访问限制
per4 = Person1("tony4",44,44,44)
per4.setMoney(88)
print(per4.getMoney())
