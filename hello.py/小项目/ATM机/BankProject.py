from BankAdimin import Admin
from BankAtm import ATM
import time

def main():

    allusers = {}

    view = Admin()
    view.LoginAdmin = "1"
    view.psd = "1"

    #开机
    view.printstar()

    #输入管理员账号
    if view.admin("login"):
        return -1

    atm = ATM()

    #选择操作
    while 1:
        view.printfunc()
        option = input("请输入您的操作: ")
        if option == "1":
            atm.creatUser()
        elif option == "2":
            atm.searchUser()
        elif option == "3":
            atm.saveMoney()
        elif option == "4":
            atm.pushMoney()
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            print("锁定")
        elif option == "8":
            print("解锁")
        elif option == "9":
            print("补卡")
        elif option == "10":
            print("销户")
        elif option == "0":
            if not view.admin("out"):
                print("退出成功")
                return -1


        time.sleep(2)


if __name__ == '__main__':
    main()
else:
    pass