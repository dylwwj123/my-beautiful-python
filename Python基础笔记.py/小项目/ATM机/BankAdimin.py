import time

class Admin(object):

    LoginAdmin = ""
    psd = ""

    def printstar(self):

        print("**************************************************************")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                         Bank                               *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("*                                                            *")
        print("**************************************************************")

    def printfunc(self):

        print("**************************************************************")
        print("*                                                            *")
        print("*    1   (开户)                                               *")
        print("*    2   (查询)                                               *")
        print("*    3   (存款)                                               *")
        print("*    4   (取款)                                               *")
        print("*    5   (转账)                                               *")
        print("*    6   (改密)                                               *")
        print("*    7   (锁定)                                               *")
        print("*    8   (解锁)                                               *")
        print("*    9   (补卡)                                               *")
        print("*    10  (销户)                                               *")
        print("*    0   (退出)                                               *")
        print("*                                                            *")
        print("**************************************************************")

    def admin(self,stuts):

        inputadmin = input("请输入管理员账号: ")

        if inputadmin == self.LoginAdmin:
            inputpsd = input("请输入管理员密码: ")
            if inputpsd == self.psd:
                if stuts == "login":
                    print("正在登录,请稍等...")
                else:
                    print("正在退出,请稍等...")
                time.sleep(2)
                return 0
            else:
                print("密码错误")
                return -1
        else:
            print("账号错误")
            return -1