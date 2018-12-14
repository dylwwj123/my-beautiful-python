import threading

def run():
    print("1111111")


t = threading.Timer(5,run)
t.start()
t.join()

print("father")