#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections.abc import abc


a = [1, 2]
a = a + [3, 4]
print("a+a ", a)

# 报错，+号两边必须都是list类型
# a = a + (5, 6)

# 就地加，不报错。+=内部采用extend实现
a += (5, 6)
print("+= ", a)

a.extend(range(2))
print("a.extend ", a)

a.append((8,9))
print("append ", a)