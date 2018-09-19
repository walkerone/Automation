# Author:zhang
# -*- coding:utf-8 -*-
import time
def test1():
    print("test1")
    time.sleep(1)
def test2(test):
    print(1111)
    test()
    print(2222)
# test1()

test2(test1)
print('---------------------')

def test3():
    print(time.time())
    print('test3')
def test4(test5):
    print(test5)
    return test5

test3=test4(test3)
print(test3)
# test3()