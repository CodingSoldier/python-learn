from collections import deque

# deque双端队列，接收iterable对象
dq = deque(["bb1", 29, 177])
ul = ("bb2", 22, 11)
# 尾部追加
dq.append(ul)
# 两个迭代对象合并，和append是不同的
dq.extend(ul)
dq.append("尾部")
dq.appendleft("头部")
# 指定下标位置插入数据，不会替换老数据，老数据往后排
dq.insert(0, "头头部")
print(dq)

# deque是线程安全的

