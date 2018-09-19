# Author:zhang
# -*- coding:utf-8 -*-
class Dog(object):
    """坎坎坷坷扩扩"""
    name='美女'
    def __init__(self, name):
        self.name = name

    #@staticmethod #静态方法和类没什么关系了
    #@classmethod
    # @property
    def eat(self):
        print("%s is eating %s" % (self.name, 'ddd'))



dog=Dog('小黑')
print(dog.__doc__)
dog.eat()
