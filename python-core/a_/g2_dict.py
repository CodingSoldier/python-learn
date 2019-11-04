#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 不建议继承list、dict
from collections import UserDict, defaultdict


class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict = MyDict(one=1)
print(my_dict)
# 初始化时，给item赋值，但是没有调用setitem，所以one的值没有乘2

# 由于setitem会乘以2，所以结果是2
my_dict["one"] = 1
print(my_dict)


# 可以使用UserDict,解决上面的问题
class MyDict2(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)

my_dict2 = MyDict2(one=1)
print(my_dict2)


# defaultdict实现了__missing__方法，没有值则返回空dict
dict3 = defaultdict(dict)
val3 = dict3["no-key"]
print(val3)




