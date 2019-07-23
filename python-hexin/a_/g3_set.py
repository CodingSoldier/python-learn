#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# set元素不重复

s = set("dafdfkjahflka")
print(s)

s2 = set(["a", "a", "b"])
print(s2)

# set简化方式
s3 = {"a", "c"}
print(type(s3))
s3.add("b")
print(s3)

# set合并
s3.update(s)
print(s3)

# s3减s
print(s3.difference(s))
# s3减s
print(s3 - s)
# 交集
print({"s"} & {"s","c"})
# 并集
print({"s", "b"} | {"s","c"})

if "s" in {"s","c"}:
    print("in")



# # 冻结的set,不可修改
# # 可以作为dict的key
# sf = frozenset("fdjakdfjla")
# print(sf)






