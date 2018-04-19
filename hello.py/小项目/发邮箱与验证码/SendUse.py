import random
from SendMessage import SendMessage

random_str = ""
for i in range(0,6):
    random_int = random.randint(0, 9)
    random_str = random_str + str(random_int)

mobile = 17611460087
text = "您的验证码是：%s。请不要把验证码泄露给其他人。" % (random_str)

send = SendMessage(mobile,text)