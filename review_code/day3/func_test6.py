# Author:zhang
# -*- coding:utf-8 -*-
def test(x,y=2):  #y是默认参数
    #默认参数特点，调用函数的时候，默认参数非必填
    print(x)
    print(y)

test(1)

def test1(*args):
    #传入多个参数
    print(args)
test1(1,2,3,4,5,6)

def test2(**kwargs):
    print(kwargs)

test2(name1='kkkkkkkkk')
