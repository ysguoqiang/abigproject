#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
 
import socket               # 导入 socket 模块
import json
 
s = socket.socket()         # 创建 socket 对象
host = 'localhost' # 获取本地主机名
port = 800                # 设置端口号
d = dict(name='Bob', age=20, score=88)
s.connect((host, port))
s.send(json.dumps(d).encode())
s.close()