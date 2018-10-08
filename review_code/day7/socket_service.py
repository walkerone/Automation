# Author:zhang
# -*- coding:utf-8 -*-
#服务端
# 就是客户端连接过来而在服务器端生成的一个连接实例
import socket
import  os
sever=socket.socket()
sever.bind(("localhost",9999))   #绑定端口号
sever.listen()  #最大连接数
print("我要开始等电话了")
while True:
    conn,addr=sever.accept()   #等待连接
    print(conn,addr)
    print("电话来了")
    while True:
        data=conn.recv(1024)
        if not data:
            print("client has lost")
            break
        print(data.decode("utf-8"))
        # res=os.popen(data).read()
        # conn.send(res)
sever.close()