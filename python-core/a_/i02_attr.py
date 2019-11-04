#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __getattr__查找不到属性的时候调用
from datetime import date

class User:

    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        print("__getattr__")
        return self.info[item]


user = User("bobby", date(year=1987, month=1, day=1), info={"edu": "master"})
user.name # 能查找到属性，不会调用__getattr__

# 没有找到edu属性，执行__getattr__，返回info中的附加信息
print(user.edu)



class User2:

    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    # 优先执行__getattribute__
    def __getattribute__(self, item):
        return "优先执行__getattribute__"

user2 =User("bobby", date(year=1987, month=1, day=1), info={"edu": "master"})
print(user2.name)






