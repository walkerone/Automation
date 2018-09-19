# Author:zhang
# -*- coding:utf-8 -*-

import json
import hashlib
sha=hashlib.sha256()
sha.update(b"zhang")
sha.update(b"honghu") #可以修改即拼接
print(sha.hexdigest())  #十六进制
sha2=hashlib.sha256()
aa="zhanghonghu索拉卡"
sha2.update(aa.encode(encoding='utf-8'))
print(type(aa))
print(sha2.hexdigest())
print(sha2.digest())
print('-----------------')
a={"zhang人":"self人"}
print(a)
a=str(a)
print(a)
sha3=hashlib.sha256()
sha3.update(a.encode(encoding="utf-8"))
print(type(a))
print(sha3.hexdigest())