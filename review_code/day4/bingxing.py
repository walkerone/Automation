# Author:zhang
# -*- coding:utf-8 -*-

def cousumer(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield
        print('包子\033[31m;1m[%s]来了被[%s] \033[0m吃了' % (baozi, name))


def producer():
    c = cousumer('zhang')
    c2 = cousumer('wang')
    c.__next__()
    c2.__next__()
    for i in range(10):
        c.send(i)
        c2.send(i)


producer()
# a = cousumer('zhang')
# b='韭菜'
# a.__next__()
# a.send(b)

# n=1
# while True:
#
#     if n <11:
#         producer()
#
#     n+=1
