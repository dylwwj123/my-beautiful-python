import time

def run():
    while True:
        print("111")
        time.sleep(1.5)


if __name__ == '__main__':

    while True:
        print("222")
        time.sleep(1)

    #不会执行到run函数，只有上面的循环结束才能执行
    run()
