#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
def get_url(url):
    # do something
    html = get_html(hrl)  # 此处暂停，切换到另一个函数去执行
    urls = parse_url(html)

传统函数调用过程  A -> B -> C
我们需要一个可以暂停的函数，并且可以在适当的时候恢复函数的继续执行
协程理解：可以暂停的函数（可以向暂停的地方传入值）

协程是在一个线程中的，避免了多线程切换。
协程可以暂停函数（比方说此时函数进行io，正在等待响应），去调用其他函数，这具备了回调的一些优点
"""



# send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
def gen_func():
    data1 = yield "数据111"
    print("2、内1", data1)
    data2 = yield "数据22"
    print("4、内2", data2)
    return "通过StopIteration.value获取返回值"

gen = gen_func()
# 通过send发送数据到生成器函数中
# 发送数据前，必须先启动一次生成器，方式有两种 1、gen.send(None), 2、next(gen)
# 第一次运行send不能传值
data1 = gen.send(None)
print("1、外1", data1)

# 这个参数竟然是穿个了data1
data2 = gen.send("参数222")
print("3、外2", data2)

try:
    data3 = gen.send("参数3333")
except StopIteration as e:
    print(e.value)
















