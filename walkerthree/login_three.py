# Author:zhang
# -*- coding:utf-8 -*-
count = 0
while True:
    name = "walker"
    password = "walker123"

    name_test = input("请输入用户名：")
    password_test = input("请输入密码")
    count += 1
    if name == name_test and password == password_test:
        print("login successful")
    elif name == name_test and password != password_test:
        print("密码错误")
        print("还有", str(3 - count), "次机会")
    elif name != name_test and password == password_test:
        print("用户名错误")
        print("还有", str(3 - count), "次机会")
    print(count)
    if count == 3:
        print("账号已被锁定")
        break
