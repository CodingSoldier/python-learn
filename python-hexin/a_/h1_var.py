#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python和java中的变量本质不一样
java变量需要指定类型，变量的内存大小就确定了，java变量相当于一个盒子
python的变量实际是一个指针，但内存大小不确定，python变量相当于一个便利贴
"""

a = 1
a = "abc"
"""
1、先生成对象，然后再贴便利贴
2、a贴1、“abc”上
"""

a = [1, 2, 3]
b = a
print(id(b) == id(a))  # a、b的id相同
print(b is a)



# 小整数，小段的值，使用全局唯一值
a = 1
b = 1
print(id(a), id(b))
a = "abc"
b = "abc"
print(id(a), id(b))

a = 156985642568
b = 156985642568
print(id(a), id(b))


a = 156985642568
b = 156985642568
print(id(a), id(b))

# 应用类型，id不相等
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(id(a), id(b))
print(a is b)  # is False
print(a == b)  # == True，调用魔法函数__eq__


