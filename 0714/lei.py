# Author:zhang
# -*- coding:utf-8 -*-
'''
类变量  类变量是直接存在类的内存中，作用，大家公用的属性,节省内存
构造函数的的变量叫实例变量（静态属性）作用于是实例本身
类的方法，功能（动态属性）
一个实例就是一个对象
类变量和实例变量相同时，类向去找的是实例变量
私有属性  是在静态属性的前面加 双下划线,在类内部可以调用，但是在类外面不能调用，私有方法和私有属相一样
私有方法  是在方法前加双下划线
析构函数，在实例，对象释放销毁的时候，或者 自动 执行的，通茶亭用于做一些收尾工作，如关闭一些数据库的链接，打开的临时文件

def __del__(self):  析构函数实在del之后或者程序结束之后执行的
'''
class a():
    # name=333
    def __init__(self,name):
        self.name1=name
        self.__ke=name
    def m(self):
        print(self.__ke)
        self.__b()
    def __b(self):
        print(self.name1)

    def __del__(self):
                # print("game over")
        pass
aa=a(44444)
del aa
