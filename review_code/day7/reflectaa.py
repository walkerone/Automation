# Author:zhang
# -*- coding:utf-8 -*-

class reflect_aaa(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating %s" % (self.name,food))


def bulk(self):
    print("%s is yelling" % self.name)
choice=input("方法：")
dog=reflect_aaa("王")

if hasattr(dog,choice):
    attr=getattr(dog,choice)
    # func("chenronghua")
    # dog.eat('张')
    dog.choice="new_name"
    setattr(dog,choice,"zhang")
    delattr(dog,choice)

else:
    setattr(dog,choice,99)
    print(getattr(dog,choice))
print(dog.name)
