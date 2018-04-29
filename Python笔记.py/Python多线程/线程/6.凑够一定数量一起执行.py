import threading
import time

bar = threading.Barrier(4)

def run():
      print("%s -- 开始" %(threading.current_thread().name))
      time.sleep(1)

      #凑够4个数执行下面代码
      bar.wait()
      
      print("%s -- 结束" %(threading.current_thread().name))


if __name__ == '__main__':
    for i in range(5):
        threading.Thread(target=run).start()