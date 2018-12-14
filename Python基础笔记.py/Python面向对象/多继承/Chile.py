from Father import Father
from Mother import Mother

class Child(Father,Mother):

    def __init__(self,hours, money, eee):
        Father.__init__(self, hours)
        Mother.__init__(self, money)

        self.eee = eee
