# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

#导入 socket、sys 模块
import socket
import sys


# 创建 socket 对象
severocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()
print("host is" + host)
port = 9999

#绑定端口
severocket.bind((host,port))

#设置最大连接数，超过后排队
severocket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr = severocket.accept()

    print("连接地址：%s",str(addr))
    msg = "欢迎C罗来到尤文图斯安联球场！" + "\r\n"

    clientsocket.send(msg.encode('utf-8'))

    clientsocket.close()

