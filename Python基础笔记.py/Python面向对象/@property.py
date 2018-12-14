
class ppp(object):

    def __init__(self,age,name):
        #属性对外暴露
        # self.age = age

        #私有属性
        self.__age = age
        self.__name = name

    #get
    @property
    def age(self):
        return self.__age
    #set
    @age.setter
    def age(self,age):
        self.__age = age

    #get
    @property
    def name(self):
        return self.__name
    #set
    @name.setter
    def name(self,name):
        self.__name = name



p = ppp(100,"www")
print(p.age)
print(p.name)
p.name = "qqq"
print(p.name)
