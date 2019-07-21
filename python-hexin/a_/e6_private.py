#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class User:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def __get_name_private(self):
        return self.__name

user = User("cpq")
print(user.get_name())
print(user._User__name)

# 属性前加上__表示私有属性，不能在类外部调用
# print(user.__name)

# 方法前面加上__表示私有方法，不能在类外部调用
# user.__get_name_private()



