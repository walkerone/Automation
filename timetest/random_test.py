#! -*- coding:utf-8 -*-
import random

print(random.random())  # 返回一个在0和1之间的小数
print(random.randint(1, 1000))  # 返回一个在1和1000之间的整数，包括1，1000
print(random.randrange(1, 20))  # 返回一个大于等于1，小于20的整数
print(random.choice((1, 2, 5, 8, 5,)))  # 从一组序列中随机查找到一个
print(random.choice([2, 5, 5, 5, 5]))
print(random.sample([1, 2, 3, 4, 5, 6, 5, 8, 9, 2], 3))
print(random.sample(range(100), 3))  # 从一个可迭代对象中返回一组数
print(range(20))  # 中range是一个可迭代对象而不是一个列表。所以python3中返回的是可迭代的对象而不是列表
print(random.uniform(1, 4))  # 返回的是在两个数之间的小数
a = [1, 2, 3, 4, 5, 6, 7]
print(random.shuffle(a))  # Shuffle list x in place, and return None.重新对列表洗牌
print(a)

checkcode = ""
for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        tmp = chr(random.randint(65, 90))
    else:
        tmp = random.randint(1, 9)
    checkcode += str(tmp)
    print(checkcode)
