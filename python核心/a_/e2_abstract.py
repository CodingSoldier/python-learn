#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import abc
from collections.abc import Sized


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass
    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisBase(CacheBase):
    # pass
    def get(self, key):
        pass
    def set(self, key, value):
        pass

redis_base = RedisBase()


"""
CacheBase是一个抽象基类，如果RedisBase不实现get、set方法，RedisBase实例化的时候会报错
python并不推荐使用抽象基类，不够灵活
推荐使用鸭子类型思想，只要这个类具有鸭子的特点，他就是鸭子
"""

class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list
    def __len__(self):
        return len(self.employee_list)

company = Company(["bobby1","bobby2"])

print(isinstance(redis_base, CacheBase))
print(isinstance(company, Sized))
"""
company也是Sized的子类，这也是python鸭子类型思想的体现
"""

print("********type*********")
# is是判断id()函数的返回值
print(type(redis_base) is RedisBase)
print(id(type(redis_base)), "==", id(RedisBase))
print(type(redis_base) is CacheBase)
print(id(type(redis_base)), "==", id(CacheBase))

# ==是判断返回值
print("********==*********")
print(type(redis_base) == RedisBase)
print(type(redis_base), "==", RedisBase)
print(type(redis_base) == CacheBase)
print(type(redis_base), "==", CacheBase)



