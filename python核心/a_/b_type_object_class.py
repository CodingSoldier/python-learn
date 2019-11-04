#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student:
    pass

class MyStudent(Student):
    pass

print("*****所有对象继承自object******")
print(MyStudent.__bases__)
print(Student.__bases__)
print(int.__bases__)
print(type.__bases__)
print(object.__bases__)   # object的基类是空

a=1


"""
1是int的实例，int是type的实例，type是type的实例。object也是type的实例
即：type创建一切
"""
print("*****type******")
print(type(1))
print(type(int))
print(type(object))
print(type(type))



