# Author:zhang
# -*- coding:utf-8 -*-
list1=[1,4,5,3,6,7,9,7]
list_1=set(list1)
list_3=set([1,3,7])
list_4=set([5,6])
list_2=set([2,6,0,66,22,8,4])
print(list_1,list_2)
print(list_1.intersection(list_2))  #交叉，交集
print(list_1.union(list_2))   #并集
print(list_1.difference(list_2))   #差集 in list_1 but not in list_2
print(list_2.difference(list_1))    #差集
print(list_1.issubset(list_3))   #是否是子集
print(list_1.issuperset(list_3))  #是否是父集

#对称差集
print(list_1.symmetric_difference(list_2))  #把互相都没有的去掉
print(list_3.isdisjoint(list_4)) #如果有交集就返回True
list_1.add(9999)
print(list_1)
list_1.update([111,222,333])
print(list_1)
list_1.discard()