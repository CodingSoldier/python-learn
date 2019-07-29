#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
asyncio是python用于解决异步io编程的一整套解决方案
tornado实现了web服务器，django+flask部署时需要配合（uwsgi、gunicorn+nginx）
"""
import asyncio
import time


# async def get_html(url):
#     print("start get url")
#     # 异步等待，非阻塞。time.sleep()是阻塞的
#     await asyncio.sleep(2)
#     print("end get url")
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("url") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time() - start_time)






# # 获取返回值，future方式
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     return "bobby"
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#
#     # # 获取返回值，future方式
#     # get_future = asyncio.ensure_future(get_html("url"))
#     # loop.run_until_complete(get_future)
#     # print(get_future.result())
#
#     # 获取返回值，task方式。task是future的子类
#     task = loop.create_task(get_html("url"))
#     loop.run_until_complete(task)
#     print(task.result())







# from functools import partial
#
# # 添加回调函数
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     return "bobby"
#
# # # 回调函数必须要有一个参数，python自动传入
# # def callback(future):
# #     print("end callback")
# #
# # if __name__ == "__main__":
# #     start_time = time.time()
# #     loop = asyncio.get_event_loop()
# #     task = loop.create_task(get_html("http://url"))
# #     # 添加回调，在get_html()运行完后运行
# #     task.add_done_callback(callback)
# #     loop.run_until_complete(task)
# #     print(task.result())
#
#
# # 回调函数接收参数，参数必须写在前面，future写在后面
# def callback(url, future):
#     print(url)
#     print("end callback")
#
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(get_html("http://url"))
#     task.add_done_callback(partial(callback, "给callback传递参数"))
#     loop.run_until_complete(task)
#     print(task.result())





# gether、wait()
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html("http://url") for i in range(10)]

    # wait()等待服务运行完
    # loop.run_until_complete(asyncio.wait(tasks))

    # gather比wait抽象程度更更高
    group1 = [get_html("http://group1111") for i in range(10)]
    group2 = [get_html("http://group2222") for i in range(10)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    # group2.cancel()

    loop.run_until_complete(asyncio.gather(group1, group2))

    print(time.time() - start_time)








