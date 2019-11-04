#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数学运算魔法函数举例，向量相加

class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        add_vector = MyVector(self.x + other.x, self.y + other.y)
        return add_vector
    def __str__(self):
        return f"x={self.x}, y={self.y}"

vec01 = MyVector(1, 2)
vec02 = MyVector(2, 3)

print(vec01 + vec02)



