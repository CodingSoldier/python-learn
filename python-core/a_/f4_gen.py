#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 普通模式生成序列
list01 = []
for i in range(21):
    if i%2 == 1:
        list01.append(i)

print(list01)


# 列表生成式，简单方便
list02 = [i for i in range(21) if i % 2 ==0 ]
print(list02)


def handle_item(item):
    return item * item

# 复杂的列表生成式，不建议写太复杂的列表生成式
list03 = [handle_item(i) for i in range(21) if i % 2 == 0]
print(list03)


# 生成器表达式
list04 = (i for i in range(21) if i % 2 == 1)
print(type(list04))
for item in list04:
    print(item)


# 字典推导式
my_dict = {"bobby1": 22, "bobby2": 23, "imooc.com": 5}
# 快速生成key、value互换字典
reversed_dict = {value:key for key, value in my_dict.items()}
print(reversed_dict)












