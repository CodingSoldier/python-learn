#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()

d = D()
print(D.__mro__)
# super并不是直接调用父类的构造函数，而是调用mro继承链中下一个类的构造函数

"""
python中也不推荐使用多继承
可以使用mixin模式（类似于java中的组合模式）
1、mixin类功能单一
2、不和基类关联，可以和任意基类组合
3、在mixin中不要使用super这种用法
"""
