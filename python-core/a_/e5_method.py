#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1
        return self.day

    # 静态方法，方法体中的Date使用了硬编码，不好，可改成类方法
    @staticmethod
    def parse_form_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))

    # 类方法，cls代表类，非硬编码
    @classmethod
    def form_string(cls, date_str):
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day))

    # 方法体中没有使用类名，没有硬编码，推荐使用静态方法
    @staticmethod
    def valid_str(date_str):
        year, month, day = tuple(date_str.split("-"))
        if int(year)>0 and (int(month) >0 and int(month)<=12) and (int(day) >0 and int(day)<=31):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

date_str = "2018-12-31"
year, month, day = tuple(date_str.split("-"))
new_date = Date(int(year), int(month), int(day))

print("实例方法", new_date.tomorrow())
print("静态方法", Date.parse_form_string(date_str))
print("类方法", Date.form_string(date_str))
print("静态方法", Date.valid_str(date_str))


