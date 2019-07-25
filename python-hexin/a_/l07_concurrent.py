#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
from concurrent.futures import as_completed, wait, FIRST_COMPLETED, ALL_COMPLETED
from concurrent.futures.thread import ThreadPoolExecutor

# futures可以让多线程和多进程编码接口一致
def get_html(times):
    time.sleep(times)
    print(f"get page {times} success")
    return times



# executor = ThreadPoolExecutor(max_workers=2)
#
# # submit能够获取线程返回结果
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))
#
# # done()方法判断任务是否完成
# print(task1.done())
#
# time.sleep(3)
# print(task1.done())
#
# # 获取线程返回结果
# print(task1.result())



# executor = ThreadPoolExecutor(max_workers=1)
# task1 = executor.submit(get_html, 3)
# task2 = executor.submit(get_html, 2)
#
# # 任务未运行，可以取消
# task2.cancel()
#
# print(task2.done())
# print(task1.done())
#




# # 列表方式
# executor = ThreadPoolExecutor(max_workers=2)
# urls = [3, 2, 4]
# all_task = [executor.submit(get_html, (url)) for url in urls]
#
# # wait(all_task, return_when=ALL_COMPLETED)  #等待所有任务完成后再执行
#
# # as_completed等待任务完成
# for future in as_completed(all_task):
#     data = future.result()
#     print(f"get page time {data}")



# map方式，最简洁
executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]

for data in executor.map(get_html, urls):
    print(f"get page time {data}")





