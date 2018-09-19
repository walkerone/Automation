# Author:zhang
# -*- coding:utf-8 -*-
school='清华'
def change():
    global school  #不要用 #声明全局变量，这样就可以在局部内修改全局变量，字符串和整数不能在局部里修改全局，字典，列表，集合都可以直接在局部修改
    print(school)
    school='北大'

change()
print(school)