#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a=["bobby01", "bobby02"]
b=("bobby03", "bobby04")

a.extend(b)
print(a)

class Company(object):
    def __init__(self, employee_list):
        self.emppoyee_list = employee_list
    def __getitem__(self, item):
        return self.emppoyee_list[item]

c=Company(["tom", "bob", "jane"])
a.extend(c)
print(a)

"""
由于Company也实现了__getitem__，c也是可迭代类型
这是python更加强大的多态
"""


