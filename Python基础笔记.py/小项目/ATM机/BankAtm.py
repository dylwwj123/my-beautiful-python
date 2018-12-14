from BankCard import Card
from BankUser import User
import random

class ATM(object):

    def __init__(self):
        self.allUsers = {}

    def creatUser(self):
        name       = input("请输入姓名: ")
        idCard     = input("请输入身份证号: ")
        phone      = input("请输入手机号: ")
        startMoney = int(input("请输入预存款金额: "))

        if startMoney <= 0:
            print("预存款金额发生错误")
            return -1

        onePsd     = input("请设置密码: ")

        if not self.checkPsd(onePsd):
            print("密码连续三次错误,开户失败")
            return -1

        cardId     = self.ranomStr()

        card111 = Card(cardId, onePsd, startMoney)
        user1 = User(name, idCard, phone, card111)

        self.allUsers[cardId] = user1

        print("开户成功！！！")
        print(self.allUsers)

    def searchUser(self):

        carNum = input("请输入您的卡号: ")

        user   = self.allUsers.get(carNum)

        if user == None:
            print("卡号不存在")
            return -1

        if not self.checkPsd(user.card.cardPassword):
            print("密码错误")
            return -1

        print("姓名: %s  余额: %d" %(user.name, user.card.cardMoney))

    def saveMoney(self):

        carNum = input("请输入您的卡号: ")

        user = self.allUsers.get(carNum)

        if user == None:
            print("卡号不存在")
            return -1

        if not self.checkPsd(user.card.cardPassword):
            print("密码错误")
            return -1

        print("余额: %d" % (user.card.cardMoney))

        nowMoney = int(input("请输入存款金额: "))

        user.card.cardMoney = user.card.cardMoney + nowMoney

        print("余额: %d" % (user.card.cardMoney))

    def pushMoney(self):

        carNum = input("请输入您的卡号: ")

        user = self.allUsers.get(carNum)

        if user == None:
            print("卡号不存在")
            return -1

        if not self.checkPsd(user.card.cardPassword):
            print("密码错误")
            return -1

        print("余额: %d" %(user.card.cardMoney))

        nowMoney = int(input("请输入取款金额: "))

        user.card.cardMoney = user.card.cardMoney-nowMoney

        print("余额: %d" %(user.card.cardMoney))

    def transfer(self):
        pass

    def changePassword(self):
        pass

    def lockUser(self):
        pass

    def unLockUser(self):
        pass

    def oldCard(self):
        pass

    def killUser(self):
        pass

    #验证密码
    def checkPsd(self,twoPsd):
        for i in range(3):
            tempPsd = input("请验证密码: ")
            if tempPsd == twoPsd:
                return 1
        return 0

    #随机卡号
    def ranomStr(self):
        random_str = ""
        for i in range(0, 6):
            random_int = random.randint(0, 9)
            random_str = random_str + str(random_int)
        return random_str