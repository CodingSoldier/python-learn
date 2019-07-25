#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from threading import RLock

total = 0

# 普通锁，同一个线程连续acquire两次，会造成死锁
# lock = threading.Lock()

# 重入锁，同一个线程中可以多次acquire，不会造成死锁，acquire多少次就得release多少次
lock = RLock()

def add():
    global lock
    global total

    for i in range(1000000):
        lock.acquire()
        dosomething()
        total += 1
        lock.release()

def desc():
    global total
    global lock

    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()

def dosomething():
    lock.acquire()
    print("dosomething")
    lock.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=desc)

t1.start()
t2.start()
t1.join()
t2.join()

print(total)








