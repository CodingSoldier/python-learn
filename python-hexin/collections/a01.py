from collections import *

"""
tuple，元组，有序列表，一旦初始化就不能修改（如果元素是对象，元素对象是可以被修改的，因为元素对象的引用id()未改变）
"""

# 实现了__iter__、或者__getitem__就是可迭代对象
name01 = ("bobby01", "bobby02")
for n in name01:
    print(n)

# 改变name01会报错
# name01[0] = "bobby3"

# 但是变量name01允许重新赋值，name01只是一个符号，不是内存区块
name01 = ("b3", "b4")


# 拆包，更容易看出元组数据的含义
user_tuple = ("bobby", 29, 175)
name, age, height = user_tuple
print(name, age, height)

# 第二种拆包使用方式
name, *other = user_tuple
print(name, other)


# 不建议将可变对象放到tuple中，tuple[1]可以被修改
tuple01 = ("bobby", [11,22])
tuple01[1].append(33)
print(tuple01)


dict01 = {}
# 当tuple完全不可变时，tuple是可哈希的，可以作为dict的key
dict01[user_tuple] = 1
print(dict01)




