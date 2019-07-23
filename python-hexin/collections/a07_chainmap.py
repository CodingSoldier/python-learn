from collections import ChainMap

d1 = {"a":"aaa", "b":"bbbb", "f":"v1111"}
d2 = {"c":"ccc", "d":"dddd", "f":"v2222"}

for key, value in d1.items():
    print(key, value)

for key, value in d2.items():
    print(key, value)

print("************")
# d2的新值不会覆盖旧值
d3 = ChainMap(d1, d2)
for key, value in d3.items():
    print(key, value)

print(d3.maps)
print(d3.maps[0]["a"])






