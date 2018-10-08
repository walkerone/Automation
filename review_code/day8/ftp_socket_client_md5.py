# Author:zhang
# -*- coding:utf-8 -*-# Author:zhang
# -*- coding:utf-8 -*-
import socket,hashlib

client = socket.socket()
client.connect(("localhost", 9999))
m=hashlib.md5()
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
        f = open(filename + "new.mp4", "wb")
        while received_size < file_total_size:
            if file_total_size-received_size>1024:
                size=1024
            else:
                size=file_total_size-received_size
                print(size)
            data = client.recv(size)
            m.update(data)
            received_size += len(data)
            f.write(data)
            print(file_total_size, received_size)
            client_file_md5=m.hexdigest()
        else:
            server_file_md5=client.recv(1024)
            print("client_md5",client_file_md5)
            print("server_md5",server_file_md5)
            print("file recv done")
            f.close()




client.close()
