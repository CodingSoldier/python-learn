#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


def callback(sleep_times):
    print(f"sleep {sleep_times}")

def stoploop(loop):
    loop.stop()

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.call_soon(callback, 2)
#     # 停止forever
#     loop.call_soon(stoploop, loop)
#     loop.run_forever()




# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     # 延迟调用
#     loop.call_later(2, callback, 2)
#     loop.call_later(1, callback, 1)
#     loop.call_later(3, callback, 3)
#     loop.run_forever()






if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()
    # 指定时间运行
    loop.call_at(now + 2, callback, 2)
    loop.call_at(now + 1, callback, 1)
    loop.call_at(now + 3, callback, 3)
    loop.run_forever()



















