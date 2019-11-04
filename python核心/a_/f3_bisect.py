#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bisect
from collections import deque

"""
bisect用于处理已经排序的序列，维持已排序序列的顺序
使用二分法
"""

inter_list = deque()
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)

# 数字4在右侧的下标位置
print(bisect.bisect(inter_list, 4))
# 数字3在左侧的下标位置
print(bisect.bisect_left(inter_list, 3))

print(inter_list)


