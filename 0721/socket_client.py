# Author:zhang
# -*- coding:utf-8 -*-
import socket
client=socket.socket()  #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
while True:
    msg=input("input in->").strip()
    if len(msg)==0:continue

    client.send(msg.encode('utf-8'))
    # client.send(msg)
    data=client.recv(1024)
    print('recv:',data)
client.close()
