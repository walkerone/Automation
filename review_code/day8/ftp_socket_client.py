# Author:zhang
# -*- coding:utf-8 -*-
import socket

client = socket.socket()
client.connect(("localhost", 9999))
while True:
    cmd = input(b"what you send", )
    if len(cmd.strip()) == 0: continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_reponse = client.recv(1024)   #返回文件大小
        print("server_reponse:", server_reponse)
        client.send(b"ready to recv file")
        print(server_reponse)
        file_total_size = int(server_reponse.decode("utf-8"))
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + ".new", "wb")
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            f.write(data)
            print(file_total_size, received_size)
        else:
            print("file recv done")
            f.close()

client.close()
