#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def exe_try():
    try:
        print("try开始")
        # raise KeyError
        return 1
    except KeyError as e:
        print("key error")
        return 2
    else:
        print("other error")
        return 3
    finally:
        print("finally")
        # return 4

# print(exe_try())



"""
上下文管理器协议
上下文管理魔法函数__enter__、__exit__
"""

class Sample:
    def __enter__(self):
        # 获取资源
        print("enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")
    def do_something(self):
        print("do something")

with Sample() as sample:
    sample.do_something()

"""
使用with语句，python解释器会先调用__enter__，执行完with方法体后，会调用__exit__
"""




