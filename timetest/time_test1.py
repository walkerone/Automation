#! -*- coding:utf-8 -*-
import time
x=time.localtime()
print(x)
print(x.tm_year)
print(time.localtime(33333333))
print(time.mktime(x))
#将结构化时间转化为格式化时间
print(time.strftime("%Y-%m-%d",time.localtime()))
#将格式化时间转化为结构化时间
print(time.strptime(time.strftime("%Y-%m-%d",time.localtime()),"%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H-%M-%S",time.localtime()))  #将结构化时间转化为格式化时间
print(time.localtime(555522200)) #将时间戳转化为结构化时间
print(time.mktime(time.localtime(550055222))) #将结构化时间转化为时间戳
print(time.asctime())
print(time.ctime())
print(time.ctime(time.time()))

x=time.localtime()
print(x)
print(time.strptime('2012-12-12 23:09:12',"%Y-%m-%d %H:%M:%S"))