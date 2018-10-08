# Author:zhang
# -*- coding:utf-8 -*-
class aaCall_aaa(object):
    name="zhang"
    def __init__(self,name):
        self.name=name
    def __call__(self, *args, **kwargs):
        print("111  %",args,kwargs)

a=aaCall_aaa("wang")
a(8,8,8,8,name="zhang")

print(aaCall_aaa.__dict__)
print(a.__dict__)