# Author:zhang
# -*- coding:utf-8 -*-
def test(x,y):
    #形参
    #形参与一一对应
    print (x)  #实参
    print(y)


test(y=2,x=1)  #这样与参数顺序无关，这是关键参数
test(2,y=2)     #位置参数和关键字参数，关键字参数在位置参数之后
