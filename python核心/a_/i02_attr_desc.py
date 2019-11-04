#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
如果user是某个类的实例，那么user.age（以及等价的getattr(user, 'age)）
首先调用__getattribute__
如果类定义了__getattr__方法，那么在__getattribute__抛出Attribute的时候会调用__getattr__
而对于描述符__get__的调用，则发生下__getattribute__内部

user = User()，那么user.age顺序如下：
1、如果age出现在User或基类的__dict__中，且age是data descriptor，那么调用其__get__方法
2、如果age出现在user的__dict__中，那么直接返回obj.__dict__["age"]
3、如果age出现在User或者其基类的__dict__中
    3.1、age是non-data descriptor，那么调用其__get__方法
    3.2、返回__dict__["age"]
4、如果User有__getattr__方法，调用__getattr__方法
5、抛出AttributeError
"""
import numbers


class IntField:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < 0:
            raise ValueError("positive value need")
        self.value = value
    def __delete__(self, instance):
        pass

class NonDataIntField:
    def __get__(self, instance, owner):
        return self.value

class User:
    age = IntField()
    # age = NonDataIntField()


user = User()
# user.age = -1  # 报错
user.age = 1   # 正常运行










