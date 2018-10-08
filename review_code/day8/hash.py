# Author:zhang
# -*- coding:utf-8 -*-
import hashlib
m=hashlib.md5()
n=hashlib.md5()
m.update(b"test")  #你好呀
m.update(b"zhang")
print(m.hexdigest())
print(n.update(b"testzhang"))
print(n.hexdigest())