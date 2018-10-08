# Author:zhang
# -*- coding:utf-8 -*-
import socket,os
import hashlib
server=socket.socket()
server.bind(("localhost",9999))
server.listen(5)   #最大连接数异步时
while True:
    conn,addr=server.accept()
    print(conn,addr)  #打印出连接对象
    while True:
        print("等待新指令")
        data=conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        cmd,filename=data.decode().split()
        print(filename)
        if os.path.isfile(filename):   #判断是否是文件
            f=open(filename,"rb")
            m=hashlib.md5()
            file_size=os.stat(filename).st_size
            conn.send(str(file_size).encode("utf-8"))   #send file size
            conn.recv(1024)   #wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5",m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode("utf-8"))

        print()
        print("send done")
server.close()