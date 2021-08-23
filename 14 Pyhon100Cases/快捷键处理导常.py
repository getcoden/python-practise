import time

try:
    while True:
        print("hello")
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\n程序运行结束')
