# Author:zhang
# -*- coding:utf-8 -*-
import copy
names=['aaa','bbbb','ccc']
print(names[0:2])  #顾头不顾尾
print(names[-1])   #区最后一个，切片
print(names[-2:-1])
names1=copy.deepcopy(names)  # 深copy  浅copy只copy一层，深copy是全部copy