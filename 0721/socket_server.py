# Author:zhang
# -*- coding:utf-8 -*-
import socket
import os
server=socket.socket()
server.bind(('localhost',6969))  #绑定端口号
server.listen()   #监听
while True:
    coon,addr=server.accept()    #实例对象
    print(coon,addr)
    while True:
        data=coon.recv(1024)

        print('data',data)
        if not data:
            print("client is lost")
            break
        res=os.popen(data).read()
        coon.send(res)
    server.close()
