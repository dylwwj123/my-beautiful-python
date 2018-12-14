from PersonClass import Person

class Son(Person):

    def __init__(self,name,age,height):
        #调用父类中的init方法
        super(Son,self).__init__(name,age)
        #自身的属性
        self.height = height