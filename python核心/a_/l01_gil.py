#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
from urllib.parse import urlparse


"""
gil global interpreter lock (cpython)
python中一个线程对应c语言中的一个线程
gil使得同一时刻只有一个线程在一个cpu上运行字节码，无法将多个线程映射到多个cpu上执行
即同一时刻只有一行字节码被运行，不可能出现多行字节码被同时运行的情况

gil会根据执行的字节码行数以及时间片释放gil，遇到io的操作时主动释放gil

"""

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

"""
每次结果都不一样
不是执行完add后再执行desc，
而是执行了一部分add后，暂停，去执行desc的代码
"""
print(total)







