#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gen_func():
    try:
        yield "url"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "result"

gen = gen_func()
print(next(gen))
gen.throw(Exception, "异常1")
print(next(gen))
# gen.throw(Exception, "异常2")































