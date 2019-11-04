from collections import OrderedDict

# OrderedDict按照添加顺序排序
# 在python3中Dict默认也是按照添加顺序排序，但是python2不是
od = OrderedDict()
od["b"] = "bbb"
od["a"] = "aaa"
od["c"] = "ccc"
od["e"] = "eee"
od["f"] = "fff"
print(od)

# entry移动到末尾
od.move_to_end("b")
print(od)

print(od.popitem())
print(od)

# 弹出值，并删除entry
print(od.pop("a"))
print(od)








