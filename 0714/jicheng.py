# Author:zhang
# -*- coding:utf-8 -*-
'''
怎样对构造函数进行继承
怎样对方法进行继承
重构父类
class people:经典类
class people(object):新式类
super是新式类的写法
python 支持多继承
python2经典类时按深度有心继承的
新式类时按广度继承的
py3 经典类，新式类都是广度优先继承的
'''


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)


class Relation(object):
    def __init__(self,a,b):
        print("执行pass")
    def make_friends(self, obj):
        print("%s is tring making friend " % self.name, obj.name)


class Man(Relation, People):
    def __init__(self, name, age):
        # People.__init__(self, name, age)    #两种继承方式
        super(Man, self).__init__(name, age)

    def piao(self):
        print("%s is eating" % self.name)

    def sleep(self):
        People.sleep(self)
        print("%s is sleeping" % self.name)


class Woman(Relation,People):
    def get_bith(self):
        print("%s is bith" % self.name)

# w1=Woman('CHENHUANRONG','26')
m1 = Man("NIUHAIYNAG", "ddd")
# m1.make_friends(w1)
# m1.eat()
# m1.piao()
# m1.sleep()
# w1 = Woman("DD", 3)
# w1.get_bith()
