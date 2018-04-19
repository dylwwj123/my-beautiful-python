
class GunClass(object):

    def __init__(self,bullet):

        self.bullet = bullet

    def shoot(self):

        if self.bullet.num > 0:

            print(self.bullet.num)

            self.bullet.num -= 1

        elif self.bullet.num == 0:

            print("子弹打没了！！")
