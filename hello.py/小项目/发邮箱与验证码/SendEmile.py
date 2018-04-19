#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#stmp服务器
stmpSever = "smtp.163.com"

#发邮件的地址
sender = "www17611460087@163.com"

#发送者邮箱密码
password = "123123wws"

#设置发送的内容
message = "wwwwwwwwwwwwwwwwwws 11110000"

#转换为邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "www"

#发送者
msg["From"] = sender


#创建smtp服务器
mailSev = smtplib.SMTP(stmpSever, 25)

#登录邮箱
mailSev.login(sender,password)

#发送
mailSev.sendmail(sender,["www17611460087@163.com"],msg.as_string())

#退出
mailSev.quit()