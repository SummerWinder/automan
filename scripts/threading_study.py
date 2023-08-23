import time, threading, multiprocessing_study as mp


def job(q):
    res = 0
    for i in range(3):
        res += i + i ** 2 + i ** 3
    q.put(res)  # queue


# 这是我们想要在一个线程中运行的函数
def print_numbers():
    for i in range(100):
        print(i)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)


# 创建线程对象，目标函数是我们刚才定义的函数
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 启动线程
thread1.start()
thread2.start()

# 等待两个线程都完成
thread1.join()
thread2.join()

if __name__ == '__main__':
    pass
    # q = mp.Queue()
    # p1 = mp.Process(target=job, args=(q,))
    # p2 = mp.Process(target=job, args=(q,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # res1 = q.get()
    # res2 = q.get()
    # print(res1 + res2)
