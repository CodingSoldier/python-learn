#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # 普通方式动态创建类
# def create_class(name):
#     if name == "user":
#         class User:
#             def __str__(self):
#                 return "user"
#         return User
#     elif name == "company":
#         class Company:
#             def __str__(self):
#                 return "company"
#         return Company
#
# MyClass = create_class("user")
# my_obj = MyClass()
# print(type(my_obj))




# def say(self):
#     return "i am user"
#
# class BaseClass():
#     def answer(self):
#         return "i am baseclass"
#
# # type动态创建类，type("类名", 父类tuple列表, 属性方法dict)
# User = type("User", (BaseClass, ), {"name":"user", "say":say})
# u = User()
# print(u.say())
# print(u.answer())



"""
元类是创建类的类
python中类的实例化过程：
    首先寻找metaclass,通过metaclass去创建类

创建User实例
    User定义了metaclass=MetaClass
    MetaClass重写了__new__魔法函数
    python使用自定义的MetaClass.__new__魔法函数创建类
"""
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "user"

my_obj = User(name="bb")
print(my_obj)









