# Author:zhang
# -*- coding:utf-8 -*-
'''
字典是无序的\
字典的增删改查
字典可以多层嵌套\
'''
info={'name':'zhang','age':22,'heitht':'190'}
# info.pop('age')  # 删除
# info.popitem()  #随机删
# print(info.get('name'))  #查询，不存在时返回NONE
# info.clear()  #清空
b={'age':'28','price':'99'}
info.setdefault('name','uuu')  #设置默认值，没有就设置
print(info.items())    #将字典转换为列表
print(dict.fromkeys(('zhang','qiang','ben'),({'age':'23','onlie':'google'})))  #修改value时所有该键值对应的都会被修改

for i in info:
    print(i,info[i])  #这样效率最快


for key,value in info.items():  #这种需要先将字典转为列表
    print(key,value)