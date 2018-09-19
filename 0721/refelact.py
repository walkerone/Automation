# Author:zhang
# -*- coding:utf-8 -*-
def bulk(self):
    print("%s is yelling" % self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("%s is eating "% self.name)


dog=Dog('niuhaiyang')
choice=input("-->")
print(hasattr(dog,choice))
if hasattr(dog,choice):
    func=getattr(dog,choice)
    func()
else:
    setattr(dog,choice,bulk)
    dog.talke(dog)
