#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
函数和类是对象，属于一等公民
一等公民：
    1、赋值给一个变量
    2、可以添加到集合对象中
    3、可以作为参数传递给函数
    4、可以当做函数的返回值
"""


def ask(name="boby"):
    print(name)

class Person:
    def __init__(self):
        print("类实例化")

def print_type(item):
    print(type(item))

# 作为函数的返回值返回
def decorator_func():
    print("decorator_func")
    return ask

# # 1、函数赋值给一个变量
# my_func = ask
# my_func("body_new")
#
# # 1、类赋值给一个变量
# my_class = Person
# my_class()


# obj_list = []
# # 对象放到集合中
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     # 放到集合中的对象可以调用
#     # print(item())
#
#     # 可作为函数参数
#     print_type(item)

my_ask = decorator_func()
my_ask("tom")



