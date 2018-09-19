# Author:zhang
# -*- coding:utf-8 -*-
import time


def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        # func()
        func(*args,**kwargs)
        stop_time = time.time()
        print('runing time is %s' % (stop_time - start_time))

    return deco


@timer
def test1():
    time.sleep(3)
    print('test1')


@timer
def test2(name):
    time.sleep(3)
    print('test2:',name)


def deco(func):
    start_time = time.time()
    # func()
    return func
    stop_time = time.time()
    print('runing time is %s' % (stop_time - start_time))


# deco(test2)
# tes1 = timer(test1)
# tes1()
# print('-----------')
test1()
test2(name='zhang')