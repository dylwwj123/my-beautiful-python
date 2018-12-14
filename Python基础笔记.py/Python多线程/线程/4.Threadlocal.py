#创建一个全局的 threading.local 对象
#每个线程独立的存储空间
#每个线程对 threading.local 对象都可以读写，但是互不影响
#作用: 它可以为每一个线程绑定一个数据库链接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以很方便的访问这些资源

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()