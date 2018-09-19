# Author:zhang
# -*- coding:utf-8 -*-
import datetime
import shelve
d=shelve.open("test_one")
info={'age':22,'job':'it'}
name=['alex',"rain","test"]
d["name"]=name
d["info"]=info
d["date"]=datetime.datetime.now()
print(d.get("info"))
print(d.get("name"))
print(d.get('date'))
for i,value in d.items():
    print(i,value)
d.close()



d.close()

