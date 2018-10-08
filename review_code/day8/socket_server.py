# Author:zhang
# -*- coding:utf-8 -*-
import socket,os
server=socket.socket()
server.bind(("localhost",9999))
server.listen(5)   #最大连接数异步时
while True:
    conn,addr=server.accept()
    print(conn,addr)
    while True:
        print("又开始了新指令")
        data=conn.recv(1024)
        if len(data.strip())==0:
            print("客户端已经断开")
            break
        print(data.decode("utf-8"))
        cmd_res=os.popen(data.decode("utf-8")).read()
        if not cmd_res:
            cmd_res="cmd_res has no output"
            conn.send(cmd_res)
        print(len(cmd_res))
        conn.send(str(len(cmd_res.encode("utf-8"))).encode("utf-8"))
        client_ack=conn.recv(1024)
        conn.send(cmd_res.encode("utf-8"))
        print("befor send")
        print(len(cmd_res))
        print("55555555555")
server.close()