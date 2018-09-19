# Author:zhang
# -*- coding:utf-8 -*-
b = (i * 2 for i in range(100000000))
print(b)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b

        n += 1
        yield b
    return '---------done'


g = fib(5)


while  True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


