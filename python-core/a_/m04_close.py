#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def gen_func():
    try:
        yield  "url"
    except BaseException:
        pass
    yield 2
    yield 3
    return "result"

if __name__ ==  "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    print("bobby")

































