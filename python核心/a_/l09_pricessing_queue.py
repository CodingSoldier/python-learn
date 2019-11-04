#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from multiprocessing import Queue, Process, Pool, Manager, Pipe


# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == "__main__":
#
#     # # 进程间通信，Queue要使用multiprocessing模块中的Queue
#     # queue = Queue(10)
#     # p = Process(target=producer, args=(queue,))
#     # c = Process(target=consumer, args=(queue,))
#     #
#     # p.start()
#     # c.start()
#     #
#     # p.join()
#     # c.join()
#
#
#     # Queue无法用于进程池间通信
#     # Manager中的Queue可以用于进程池通信
#
#     # queue = Queue(10)
#     queue = Manager().Queue(10)
#     pool = Pool(2)
#     pool.apply_async(producer, args=(queue,))
#     pool.apply_async(consumer, args=(queue,))
#     pool.close()
#     pool.join()








# def producer(pipe):
#     pipe.send("共享数据")
#
# def consumer(pipe):
#     print(pipe.recv())
#
# if __name__ == "__main__":
#
#     # 使用pipe实现进程间通信
#     recevie_pipe, send_pipe = Pipe()
#     p = Process(target=producer, args=(send_pipe,))
#     c = Process(target=consumer, args=(recevie_pipe,))
#
#     p.start()
#     c.start()
#     p.join()
#     c.join()
#







# 使用Manager().dict()实现数据结构通信
def add_data(p_dict, key, value):
    p_dict[key]  = value

if __name__ == "__main__":
    progress_dict = Manager().dict()
    p1 = Process(target=add_data, args=(progress_dict, "age", 11))
    p2 = Process(target=add_data, args=(progress_dict, "age", 22))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(progress_dict)






# # 共享变量不能用于进程间通信，因为进程间的数据是隔离的
# def producer(a):
#     a += 100
#     time.sleep(2)
#
# def consumer(a):
#     time.sleep(2)
#     print(a)
#
# if __name__ == "__main__":
#     a = 1
#     my_producer = Process(target=producer, args=(a,))
#     my_consumer = Process(target=consumer, args=(a,))
#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()










