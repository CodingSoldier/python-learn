#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numbers
"""
通过实现__getitem__来实现切片
"""

# 实现一个不可修改序列
class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    # 翻转
    def __reversed__(self):
        self.staffs.reverse()

    # 长度
    def __len__(self):
        return len(self.staffs)

    # 迭代，暂不详解
    def __iter__(self):
        return iter(self.staffs)

    # 包含
    def __contains__(self, item):
        return True if (item in self.staffs) else False

    # 实现切片
    def __getitem__(self, item):
        # 获取类名，避免硬编码Group
        cls = type(self)
        # slice是python内置的切片对象，当使用切片时，item是slice类型的实例
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        # group[0]这时候item是数字0，即整数类型
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

staffs = ["bobby1", "imooc", "bobby2", "bobby3"]
group = Group("imooc", "user", staffs)
print(group[0])
print(group[:2])
pass





