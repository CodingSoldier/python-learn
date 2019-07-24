#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""
函数的工作原理
python.ext会用一个叫做 PyEval_EvalFramEx(c函数)去执行foo函数，首先会创建一个栈帧
python中一切皆对象，栈帧、字节码都是对象
当foo调用子函数bar，又会创建一个栈帧
所有栈帧都分配到堆内存上，堆内存的对象不会随着函数调用结束而删除，这就决定了栈帧可以独立于调用者存在
"""
import dis
import inspect

# frame = None
# def foo():
#     bar()
#
# def bar():
#     global frame
#     frame = inspect.currentframe()
#
# # 查看字节码
# print(dis.dis(foo))
#
# foo()
# # foo函数执行结束，但是一节可以获取到bar函数
# print(frame.f_code.co_name)
# # f_back获取上一个调用者
# print(frame.f_back.f_code.co_name)



def gen_fn():
    yield 1
    name = "bb"
    yield 2
    age = 30
    return "imooc"

print(dis.dis(gen_fn))

gen = gen_fn()
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

# 执行下一个栈帧
next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

next(gen)
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)


"""
yield在遍历的使用
_collections_abc.Sequence#__iter__

    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return

"""






