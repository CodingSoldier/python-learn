# -*- coding: utf-8 -*-
#
# # 放到linux环境运行
# import os
#
# pid = os.fork()
#
# """
# 运行fork，子进程会拷贝父进程的运行代码，所有打印了两次“运行”
# print("运行")放到fork前，只会运行一次
# """
# print("运行")
#
# if pid == 0:
#     print('子进程{}, 父进程{}'.format(os.getpid(), os.getppid()))
# else:
#     print('我是父进程{}'.format(pid))
#








import multiprocessing
import time


def get_time(n):
    print(f"子进程~~{n}~~")
    time.sleep(n)
    return n

if __name__ == "__main__":

    # progress = multiprocessing.Process(target=get_time, args=(2,))
    # print("为start前，没有pid", progress.pid)
    # progress.start()
    # print("pid ", progress.pid)
    # progress.join()
    # print("主进程结束")

    # # 使用线程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())


    # result = pool.apply_async(get_time, args=(3, ))
    # # 等待所有任务完成才能调用join()
    # pool.close()
    # pool.join()
    # print(result.get())


    # for result in pool.imap(get_time, [1, 5, 3]):
    #     print("返回结果 ", result)


    for result in pool.imap_unordered(get_time, [1, 5, 3]):
        print("返回结果  ", result)















