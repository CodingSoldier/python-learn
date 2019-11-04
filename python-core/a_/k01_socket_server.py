#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
应用层协议：HTTP、FTP、SMTP、DNS等协议
传输层协议：TCP、UDP协议

应用层协议是在传输层的基础上再次封装
TCP支持通信双方建立连接后保持连接状态不挂断，但应用层可能封装这种协议
所以出现了socket，各大操作系统提供了操作传输层协议的api接口，
通过socket使用这些接口
"""
import socket

# 服务端
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8000))
server.listen()
sock, addr = server.accept()

while True:
    data = sock.recv(1024)
    print(data.decode("utf8"))
    re_data = input()
    sock.send(re_data.encode("utf8"))

    # server.close()
    # sock.close()








