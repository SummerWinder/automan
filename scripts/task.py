import datetime
import time, threading_study as td, multiprocessing_study as mp

"""使用while循环做检测某个参数的变化"""


def wait():
    var = 0
    while True:
        if var == 100000000:
            print(time.time())
            break
        else:
            var += 1
            continue


def task():
    scheduled()
    now = time.strftime('%H:%M:%S', time.localtime())
    print('first time is:', now)
    time.sleep(3)
    print('second time is:', now)


def scheduled():
    t = td.Timer(2, task)
    t.start()


scheduled()
