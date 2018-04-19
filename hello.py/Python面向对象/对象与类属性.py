from types import MethodType

class cla(object):

    #这里的属性为类属性
    #用类名来调用
    name = "111"

    def __init__(self,name):
        #对象属性
        #添加属性 self对象
        self.name = name


def addmthod(self):
    print("add")

print(cla.name)

c = cla("222")
#动态的给对象添加属性
c.age = 18
print(c.name)
print(c.age)

#动态添加方法
c.add = MethodType(addmthod,c)
c.add()

#限制动态添加的属性
class cla1(object):

    __slots__ = ("name","age")


c1 = cla1()
c1.name = 44
print(c1.name)

