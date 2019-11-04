#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:

            self.cond.wait()
            print(f"{self.name} : 在")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name} : 好啊")
            self.cond.notify()

            self.cond.wait()
            print(f"{self.name} : 君住长江尾")
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print(f"{self.name} : 小爱同学")
            self.cond.notify()
            time.sleep(2)
            self.cond.wait()

            print(f"{self.name} : 我们来对古诗吧")
            self.cond.notify()
            self.cond.wait()

            print(f"{self.name} : 我住长江头")
            self.cond.notify()
            self.cond.wait()

cond = threading.Condition()

xiaoai = XiaoAi(cond)
tianmao = TianMao(cond)

"""
先启动小爱，再启动天猫精灵
如果天猫精灵先启动
    print(f"{self.name} : 小爱同学")
    self.cond.notify()   此时小爱可能未启动，无法唤醒任何线程
    self.cond.wait()     天猫等待其他线程唤醒
小爱启动
    self.cond.wait()   等待其他持锁线程唤醒，但无持锁线程唤醒，一直等待
    print(f"{self.name} : 在")
    self.cond.notify() 
    
with cond 是对lock.acquire()，lock.release()的封装
在调用with cond 之后才能调用wait()、notify()

condition有两层锁，threading.Condition()初始化时创建一把锁，XiaoAi、 TianMao共用这把锁
XiaoAi.wait()时
    1、释放Condition公共锁
    2、生成一把新锁，放到公共队列中，锁住当前线程
TianMao线程获得锁后继续执行，运行到notify()
    1、释放公共队列中的一个，此时XiaoAi线程生成锁住自身的锁被释放，等待Condition公共锁释放即可运行
TianMao继续运行，运行wait()    
    1、释放Condition公共锁
    2、生成一把新锁，放到公共队列中，锁住当前线程TianMao
    
    3、XiaoAi获取到Condition锁，继续运行    
               
"""
xiaoai.start()
tianmao.start()



