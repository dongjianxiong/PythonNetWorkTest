# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
client.connect((host, port))

# 接收小于 1024 字节的数据
msg = client.recv(1024)

client.close()

print (msg.decode('utf-8'))