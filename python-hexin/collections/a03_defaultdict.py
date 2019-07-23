

# 普通dict做统计
from collections import defaultdict

dict1 = {}
dict2 = {}
ul = ["b1","b0","b4","b1","b1","b4"]

for u in ul:
    if u not in dict1:
        dict1[u] = 1
    else:
        dict1[u] += 1

for u in ul:
    dict2.setdefault(u, 0)
    dict2[u] += 1

print(dict1)
print(dict2)



# 当key不存在是初始化，key的value为int初始值0
default_dict= defaultdict(int)
for u in ul:
    default_dict[u] += 1

print(default_dict)


# 通过函数返回值自定义defaultdict默认值
def get_defaultdict():
    return {
        "name": "",
        "age": 0
    }

default_dict = defaultdict(get_defaultdict)
print(default_dict["a"])


