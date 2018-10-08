# Author:zhang
# -*- coding:utf-8 -*-

# class FOO(object):
#     def __init__(self,name):
#         self.name=name
#
# f=FOO("ZHANG")
# print(type(f))
# print(type(FOO))
#
#
# print('------------')
def func(self):
    print("i am func %s" % self.name)

def __init__(self,name):
    self.name=name

aaa=type('aaa',(object,),{"talk":func,"__init__":__init__})
f=aaa("zhang")
f.talk()
print(type(f))