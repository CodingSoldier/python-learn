#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    # 动态属性，可以使用user.age这种方式获取值
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

user = User("bobby", date(year=1987, month=1, day=1))
print(user.age)











