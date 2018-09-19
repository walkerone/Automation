# Author:zhang
# -*- coding:utf-8 -*-

data={}
data1=[]
try:
    data1[2]
    data['name']
    data1[3]
except KeyError as e:
    print('%s is no here'%  e)
except IndexError as m:
    print('%s is out of range' % m)