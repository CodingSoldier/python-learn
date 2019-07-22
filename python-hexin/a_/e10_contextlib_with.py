#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import contextlib

"""
使用contextlib和yield实现上下文管理器
"""
@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("xxx.txt") as f:
    print("file processing")



