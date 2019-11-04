#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
切片 [start:end:step]

start表示切片开始位置，默认为0
end表示切片截止（但不包括）位置（默认为列表长度）
step表示切片的步长（默认为1）

当start为0是可以省略
当end为列表长度时可以省略
当step为1时可以省略，省略步长时，可以省略最后一个冒号
当step为负数是2，表示反向切片，这时start比end大
"""

aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
# 返回源列表中所有元素的新列表
print(  aList[:])
print(  aList[::])
# 逆序新列表
print(aList[::-1])
# 取偶数位置
print(aList[::2])
# 取奇数位置
print(aList[1::2])
# 指定开始结束位置
print(aList[3:6])
# 切片结束位置大于列表长度，从列表尾部截断
print(aList[0:100])
# 切片开始位置大于列表长度，返回空列表
print(aList[100:])

# 列表末尾追加元素
aList[len(aList):] = [9]
print(aList)

# 列表头部插入元素
aList[:0] = [1,2]
print(aList)

# 列表中间位置插入元素
aList[3:3] = [33]
print(aList)

# 替换列表左边元素
aList[:3] = [1, 2]
print(aList)

# 替换列表右边元素
aList[3:] = [4, 5, 6]
print(aList)

# 隔一个改一个
aList[::2] = [0] * 3
print(aList)

# 删除列表前3个元素
aList[:3] = []
print(aList)


# 删除下标前面的元素
bList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
del bList[:3]
print(bList)

# 从0开始，步长为2倍数的元素删除掉
del bList[::2]
print(bList)







