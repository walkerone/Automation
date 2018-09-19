# Author:zhang
# -*- coding:utf-8 -*-
import hashlib
import hmac
m=hashlib.sha256()
m.update( "kkkkkkkkkkk老师发的kkkkkk".encode("utf-8"))
print(m.hexdigest())

n=hmac.new(b"III",'KKKK强'.encode(encoding="UTF-8"))
print(n.digest())