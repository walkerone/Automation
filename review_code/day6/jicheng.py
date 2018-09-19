# Author:zhang
# -*- coding:utf-8 -*-

class People(object):  # 新式类的写法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def sleep(self):
        print("%s is sleeping" % self.name)


class Relation(object):
    def make_friends(self, obj):
        print("%s is make friend with %s" % (self.name, obj.name))
        print(obj)
        self.friends.append(obj)  # 为什么是obj


class Man(People, Relation):
    def __init__(self, name, age, money):  # 重构构造函数,money新增的属性
        # People.__init__(self.name,age)
        super(Man, self).__init__(name, age)  # 另一种方式
        self.money = money

    def piao(self):
        print("%s is piao.....20..........done" % self.name)

    def sleep(self):  # 重构父类的方法
        People.sleep(self)  # 执行父类的方法
        print("%s is sleep %d miutes" % (self.name, 33))


class Woman(People, Relation):
    def get_birth(self):
        print('%s is birth last day' % self.name)


#
m = Man('zhang', 'dd', 'ee')
m.sleep()
#
w = Woman('white', 334)
print('----------')
# w.get_birth()
m.make_friends(w)
print(m.friends[0])
