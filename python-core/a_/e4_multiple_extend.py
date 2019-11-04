#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python使用C3算法实现继承

class D1:
    pass

class C1(D1):
    pass

class B1(D1):
    pass

class A1(B1, C1):
    pass

print("菱形继承", A1.__mro__)


class E2:
    pass

class D2:
    pass

class C2(E2):
    pass

class B2(D2):
    pass

class A2(B2, C2):
    pass

print("双继承", A2.__mro__)








