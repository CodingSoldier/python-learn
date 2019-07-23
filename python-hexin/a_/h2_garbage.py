#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# cpython中使用垃圾回收算法使用 引用计数
a = object()
b = a
# object()的引用计数是2

del a    # object()的引用计数减1，是1

print(b) # 能找到object()，object未被删除
# print(a)  # 报错，a变量已经被删除了

















