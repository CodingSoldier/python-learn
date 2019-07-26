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







