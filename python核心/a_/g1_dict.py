#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
from collections.abc import Mapping, MutableMapping


"""
dict并没有继承MutableMapping，而是实现了MutableMapping的一些魔法函数
"""
a = {}
print( isinstance(a, MutableMapping) )




b = {
    "bobby1": {
        "company": "imooc"
    },
    "bobby2": {
        "company": "imooc2"
    }
}

# 浅拷贝
# b2 = b.copy()
# 深拷贝
b2 = copy.deepcopy(b)
b2["bobby1"]["company"]="imooc3"
print(b)




# formkeys，用可迭代对象作为key生成新字典
new_list = ["bobby1", "bobby2"]
new_list = dict.fromkeys(new_list, {"company": "imooc"})
print("new_list  ", new_list)

# 没有key，抛异常
# print(new_list["bobby"])
# 没有key返回默认值
print(new_list.get("bobby", {}))

# key不存在，插入键值，并返回新设置的值1
print(new_list.setdefault("bobby", 1))
print(new_list)
# key存在，返回key对应的value值，不设置新值
print(new_list.setdefault("bobby1", 1))
print(new_list)



b3 = {
    "key1": {
        "c": "imooc"
    },
    "key2": {
        "c": "imooc2"
    }
}
b3.update({"k": "v"})
b3.update((("k02","v02"),))
print("b3  ", b3)





