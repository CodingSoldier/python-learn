#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect

# 生成器可以接受参数，可以返回数据，还可以暂停。这就跟线程很像了，可以当做协程
def gen_func():
    value = yield 1
    print("gen_func  ", value)
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    # 获取协程状态
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration:
        pass
    print(inspect.getgeneratorstate(gen))























