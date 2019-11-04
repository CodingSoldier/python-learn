from collections import Counter

# Counter计数器
ul = ["b1","b0","b4","b1","b1","b4"]
uc = Counter(ul)
print(uc)

# 统计字符串
str = Counter("djfkajhfidhaajskfhkd24935795")
print(str)

# 追加
str.update("djfkajhfidh")
print(str)

# Counter本身也是一个可迭代对象，可以作为update参数
str.update(str)
print(str)

# top n 统计问题
print(str.most_common(2))
