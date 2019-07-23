#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 一个经典的错误
class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self, staff_name):
        self.staffs.append(staff_name)
    def remove(self, staff_name):
        self.staffs.remove(staff_name)

com1 = Company("com1")
com1.add("员工壹")

com2 = Company("com2")
com2.add("员工二")

"""
由于初始化Company的时候没有指定staffs，所以com1、com2使用了默认的staffs=[]
导致修改com1、com2之间的修改会相互影响
"""
print(com1.staffs == com2.staffs)
print(com1.staffs)
print(com2.staffs)

# 初始化一个staffs，不会相互影响
com3 = Company("com3", ["初始化员工1"])
com3.add("员工二")
print(com3.staffs)

#######不推荐在类初始化时传递一个引用类型这种写法###############




#
# def add(a, b):
#     a += b
#     return a
#
# a = 1
# b = 2
# # a的值不受影响
# print(a, b, add(a, b))
#
# a = (1, 2)
# b = (3, 4)
# # a的值不受影响
# print(a, b, add(a, b))
#
# a = [1, 2]
# b = [3, 4]
# # a的值受函数影响
# print(a, b, add(a, b))
#










