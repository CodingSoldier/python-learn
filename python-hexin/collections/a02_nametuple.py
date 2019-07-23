from collections import namedtuple

# 使用namedtuple快速创建一个简单类User
User = namedtuple("User", ["name", "age", "height"])
user_tuple = User(name="bobby", age=29, height=175)
print(user_tuple.name, user_tuple.age, user_tuple.height)


User2 = namedtuple("User", ["name", "age", "height", "edu"])
u2 = ("bobby", 29, 175)
# 使用tuple传参，单*号
u2 = User2(*u2, "master")
print(u2.name, u2.age, u2.height, u2.edu)


# 使用dict传参，双**号
dict3 = {
    "name": "bb",
    "age": 29,
    "height": 175,
}
u3 = User2(**dict3, edu="master")
print(u3)


dict4 = {
    "name": "u4",
    "age": 44,
    "height": 175,
    "edu": "master"
}
tuple4 = ("u4", 22, 175, "master")
# _make接收可迭代对象，不需要加*，但是接收dict类型有问题
u4 = User2._make(dict4)
print("u4  ", u4)
# _make接收tuple、list就没问题
u4 = User2._make(tuple4)
print("u4  ", u4)


# User转dict
user_dict = u4._asdict()
print(user_dict)


# 拆包功能
name, age, *other = u4
print(name, age, *other)


# *args和**kwarks
def ask(*args, **kwarks):
    pass

# *args使用tuple接收参数
ask("name", 60)

# **kwarks使用dict接收参数
ask(name="name01", age=60)










