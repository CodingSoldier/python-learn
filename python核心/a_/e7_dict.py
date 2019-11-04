#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

stu = Student("小明")
# stu.__dict__只能获取到Student中定义的属性，不能获取父类的属性
print("stu.__dict__  ", stu.__dict__)
# Person.__dict__类属性很多
print("Person.__dict__  ", Person.__dict__)

# dir可以获取属性key
print("dir(stu)  ", dir(stu))
print("dir(Person)  ", dir(Person))


