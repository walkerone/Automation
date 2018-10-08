# Author:zhang
# -*- coding:utf-8 -*-

class Dog(object):
    def __init__(self, name):
        self.name = name
        self.food = None

    @property
    def eat(self):
        print(self.name,"is eating %s"% self.food)
    @eat.setter
    def eat(self,food):
        self.food=food
        print("eat'settle")
    @eat.deleter
    def eat(self):
        del self.food
        print("删除完了")
dog1=Dog("WANG")
dog1.eat
dog1.eat="面包"
dog1.eat
del  dog1.eat


