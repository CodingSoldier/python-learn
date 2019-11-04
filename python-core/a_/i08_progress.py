#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多进程编程
进程切换代价高于线程
耗cpu的操作，多进程编程可以使用多核优势
对于io操作，多线程优于多进程
"""
import time
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

# windows下使用进程，需要加上 if __name__ == "__main__"
if __name__ == "__main__":
    # with ThreadPoolExecutor(3) as executor:
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25,40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))






