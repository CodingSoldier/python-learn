#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
import time

"""
在遇到io的时候回释放锁，发送网络请求也是一种io，所以python写爬虫效率比较高
"""

def get_detail_html(url):
    print("列表获取 start")
    time.sleep(2)
    print("列表获取 end")

def get_detail_url(url):
    print("详情获取 start")
    time.sleep(2)
    print("详情获取 end")

t1 = threading.Thread(target=get_detail_html, args=("",))
t2 = threading.Thread(target=get_detail_url, args=("",))

start_time = time.time()

# # __main__线程运行完成，t1、t2未运行完成，程序不会退出。等到t1、t2运行完成才退出
# t1.start()
# t2.start()

# # t1、t2设置为守护进程，主进程结束，t1、t2会被强制结束
# t1.setDaemon(True)
# t2.setDaemon(True)
# t1.start()
# t2.start()

# 等待t1、t2运行结束，当前线程才继续执行
t1.start()
t2.start()
t1.join()
t2.join()


print("运行时间 ", time.time() - start_time)













