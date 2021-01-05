#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py
 
import socket               # 导入 socket 模块
 
s = socket.socket()         # 创建 socket 对象
host = "127.0.0.1" #socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
 
s.listen(5)                 # 等待客户端连接
c,addr = s.accept()     # 建立客户端连接
while True:
    # print('连接地址：', addr)
    val = c.recv(100)
    if val:
        print(val.decode())
        c.send(val)
    # c.send('欢迎访问菜鸟教程！'.encode())
    # c.close()                # 关闭连接