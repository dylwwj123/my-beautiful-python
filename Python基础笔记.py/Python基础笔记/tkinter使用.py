import tkinter

win = tkinter.Tk()

win.title("啊啊啊啊啊啊啊")

win.geometry("400x400+530+260")

#Lable ***********************************************
lab1 = tkinter.Label(win,
                     text = "啊啊啊啊啊啊啊啊啊啊啊啊啊啊!!", #文本
                     bg = "black", #背景色
                     fg = "green", #字体色
                     font = ("黑体",20), #字体 字体大小
                     width = 20, #宽
                     height = 5, #高
                     wraplength = 100, #换行宽度
                     justify = "left", #换行左对齐
                     anchor = "w", #文本对齐 n上 e右 s下 w左 center居中
                    )
# lab1.pack()

#Button ***********************************************
def btn1Sel():
    print("点我弄啥嘞!!")

btn1 = tkinter.Button(win,
                      text = "点我点我!!",
                      command = btn1Sel)

# btn1.pack()

#Entry ***********************************************
ee = tkinter.Variable()
#show = "*" 密文
entry = tkinter.Entry(win, textvariable=ee)
entry.pack()

ee.set("aaaaaaaa")



win.mainloop()