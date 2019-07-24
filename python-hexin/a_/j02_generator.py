#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def generator_fn():
#     yield 1
#     yield 2
#     yield 3
#
# def normal_fn():
#     return 1
#
# gen = generator_fn()
# """
# 只要函数中有yield关键字，此函数就是 生成器函数
# 生成器函数返回结果是生成器对象，生成器对象也是一个可迭代对象
# 生成器函数中使用几次yield，返回结果(可迭代对象)中就会有几个元素
# 生成器对象在python编译字节码的时候产生
# """
# print(gen)
# for value in gen:
#     print(value)
#
# result = normal_fn()
# print(result)
#




# 返回一个值的斐波那契数列
def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index -1) + fib(index - 2)

print(fib(8))



# 返回一个斐波那契的list，如果index很大，返回的list也会很大，消耗内存
def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

print(fib2(8))



# 使用yield是一个一个地返回，不会造成内存占用高
def fib_gen(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1

print("*********fib_gen***********")
for data in fib_gen(8):
    print(data)



