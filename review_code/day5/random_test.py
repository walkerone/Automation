# Author:zhang
# -*- coding:utf-8 -*-
import random

random.randint(1,10)  #返回1--》10之间的数包括1,10
print(random.randrange(1,2))   #顾头不顾尾
print(random.choice([1,2,3]))  #从序列中随机找一个值

print(random.sample([1,2,3],2))  #随机取两个值

random.shuffle([1,2,5,8,7,4,1])  #洗牌列表
print(random.randint(1,2))
print('\033[32m-------------------\033[0m')
checkcode=''
for i in range(4):
    current_code=random.randint(1,4)
    if i==current_code:
        temp=random.randint(0,9)
    else:
        temp=random.randint(65,90)
        temp=chr(temp)
    checkcode+=str(temp)
print(checkcode)

print('---------------')
import sys
print(sys.argv)  #读取参数