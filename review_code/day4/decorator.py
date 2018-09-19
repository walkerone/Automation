# Author:zhang
# -*- coding:utf-8 -*-
import time


def test2():
    print(time.time())
    return time.time()


@test2
def test1():
    print("first one")


test1()
