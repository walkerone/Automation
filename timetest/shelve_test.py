# Author:zhang
# -*- coding:utf-8 -*-
import datetime
import shelve
d=shelve.open("test_one")
print(d.get("info"))
print(d.get("name"))
print(d.get('date'))
# info={'age':22,'job':'it'}
# name=['alex',"rain","test"]
# d["name"]=name
# d["info"]=info
# d["date"]=datetime.datetime.now()
# d.close()

print(d.get("name"))