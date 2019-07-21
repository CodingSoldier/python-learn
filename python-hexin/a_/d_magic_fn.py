#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python的内置魔法函数以__开头，__结尾
魔法函数增强了类的特性
不要自定义魔法函数，使用python内置魔法函数即可
"""
class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self, item):
        return self.employee_list[item]

company = Company(["tom", "bob", "jane"])

# 调用company的__getitem__方法，抛异常后退出for循环
for em in company:
    print(em)



