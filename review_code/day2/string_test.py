# Author:zhang
# -*- coding:utf-8 -*-
# name1=input()
name='my \tnamNey is ales %s\n'

print(name.center(50,'-'))  # 设置长度，两边补-
print(name.count('my'))   #打印字符串数量
print(name.endswith('es'))  #以什么结尾  返回布尔值
print(name.expandtabs(19))  #tab键之后的空格长度
print(name.find('y'))   #返回小写的位置
print(name.format())    #格式化
# print(name.format_map({'zhang':2222})) #字典式格式化
print(name.index('is'))   # 返回下标
print(name.isalnum())  #返回布尔值，检查是否由字母和数字组成
print(name.isupper())    #返回是否大写true或false
print('333BH'.isdecimal())  #返回是否是十进制数
print(name.isdigit())  #检查是否是数字
print(name.isidentifier())  #检查是否是合法标识，变量名
print('11'.isnumeric())
# print(name.join())  #？
print(name.ljust(100,'-'))  #设置长度，不够左边以什么补齐
print(name.lower())    #大写变小写
print(name.lstrip())  #省略左边的空格和换行符
print(name.strip())    #省略两头的空格和换行符
print('33333333 ')
print(name.split(' '))  #以参数作为分隔符返回列表
print(name.swapcase())  #反转，大写变小写，小写变大写
print(name.replace('my','kk'))  #替换
