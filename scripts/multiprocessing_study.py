import multiprocessing


def worker(num):
    """子进程要执行的任务"""
    print(f"Worker {num} is running")
    return


if __name__ == '__main__':
    # 创建4个子进程
    processes = []
    for i in range(100):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

        # 等待所有子进程结束
    for p in processes:
        p.join()