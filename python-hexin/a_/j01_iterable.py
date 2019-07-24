#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import Iterable, Iterator

"""
迭代器是访问集合内元素的一种方式，一般用来遍历数据
迭代器和以下边的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性访问数据的方式
"""

# a = [1, 2]
#
# """
# Iterable可迭代对象
# 定义了__iter__虚拟方法
# """
# print(isinstance(a, Iterable))  # list是可迭代类型
#
#
# """
# Iterator迭代器，继承自Iterable
# 新增了__next__虚拟方法
# """
# print(isinstance(a, Iterator))  # list不是迭代器，没有实现__next__方法，也就没有 a.next() 这种方法
#



# class Company(object):
#     def __init__(self, employee_list):
#         self.employee = employee_list
#
#     def __getitem__(self, item):
#         return self.employee[item]
#
#
#
# company = Company(["ab", "cd", "efg"])
# for item in company:
#     print(item)
#
# # 可迭代，但不是Iterable、Iterator
# print(isinstance(company, Iterable))
# print(isinstance(company, Iterator))
#
# iter01 = iter(company)
# # 使用iter()转换为迭代器
# print(isinstance(iter01, Iterable))
# print(isinstance(iter01, Iterator))








# 自定义迭代器

class MyIterator(Iterator):
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.index = 0
    def __next__(self):
        # 迭代逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

company = Company(["tom", "bob", "jane"])
my_iter = iter(company)

# # 使用while模拟for循环
# while True:
#     try:
#         print(next(my_iter))
#     except StopIteration:
#         pass
#

for item in company:
    print(item)





