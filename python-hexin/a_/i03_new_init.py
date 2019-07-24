#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
new用来控制对象的生成过程，在对象生成之前
init用来完善对象
如果new方法不返回对象，则不会调用init
"""
class User:
    def __new__(cls, *args, **kwargs):
        print(" in new ")
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name
        print("in init")

user = User(name="bb")













