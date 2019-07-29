#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bobby1": "value1",
    "bobby2": "value2",
}

# # chain所有可迭代对象
# for value in chain(my_list, my_dict, range(5, 10)):
#     print(value)




# # chain的原理
# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         for value in my_iterable:
#             yield value
#
# for value in my_chain(my_list, my_dict, range(5, 10)):
#     print(value)





# yield from iterable，从迭代对象中yield出元素
def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable

for value in my_chain(my_list, my_dict, range(5, 10)):
    print(value)


























