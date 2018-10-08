# Author:zhang
# -*- coding:utf-8 -*-k
import  socket
client=socket.socket()
client.connect(("localhost",9999))
while True:
    fasong=input("what you fasong")
    # if len(fasong.strip())==0:continue
    client.send(fasong.encode("utf-8"))
    data=client.recv(1024)
    print(data.decode("utf-8"))
client.close()