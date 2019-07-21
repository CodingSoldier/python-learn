#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python多态并不需要继承同一个父类，只要这些类都有同一个方法即可
python中的鸭子类型：
    当看到一只鸟走起来像鸭子、游泳像鸭子、叫声像鸭子，
    那么这只鸟就可以被称为鸭子
"""
class Cat(object):
    def say(self):
        print("i am a cat")

class Dog(object):
    def say(self):
        print("i am a fish")

class Duck(object):
    def say(self):
        print("i am a duck")

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()



