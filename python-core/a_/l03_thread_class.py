#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

# 线程类
class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")

t1 = GetDetailHtml("t1")
t2 = GetDetailUrl("t2")

start_time = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

print("运行时间 ", time.time() - start_time)












