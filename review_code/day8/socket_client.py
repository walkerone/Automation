# Author:zhang
# -*- coding:utf-8 -*-
import socket

client = socket.socket()
client.connect(("localhost", 9999))
while True:
    data = input(b"what you send", )
    if len(data.strip()) == 0:
        continue
    client.send(data.encode("utf-8"))
    cmd_res_data = client.recv(500)   #接收命令结果的长度
    client.send("收到".encode("utf-8"))
    print("命令结果大小",cmd_res_data)
    receive_size = 0
    receive_date = b''
    while receive_size < int(len(cmd_res_data.decode("utf-8"))):
        data = client.recv(500)
        receive_size += len(data)
        receive_date += data
        print(receive_size)
        print(receive_date.decode())
    else:
        print("cmd res receive done",receive_size)
        print(receive_date.decode())

client.close()
