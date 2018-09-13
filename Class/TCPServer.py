# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

from socket import *
from time import ctime

host = ''
port = 12345
buffsize = 2048
ADDR = (host,port)

tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(ADDR)
tctime.listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient,addr = tctime.accept()
    print("Connection from :",addr)

    while True:
        data = tctimeClient.recv(buffsize).decode()
        if not data:
            break

        tctimeClient.send(('回复：[%s] %s' % (ctime(),data)).encode())
    tctimeClient.close()
tctimeClient.close()