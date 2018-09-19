# Author:zhang
# -*- coding:utf-8 -*-
import time
import datetime
time1=time.time()   #f返回时间戳
time.sleep(1)   #休息几秒
time2=time.gmtime()   #返回utc时区的，时间戳转换为元组d的形式
time3=time.localtime()  #返回当前时区的时间，返回一个元组的形式
print(time1)
print(time2)
print(time.localtime(5555555555))
print(time.mktime(time3))   #元组形式的转换为时间戳
print(time.strftime("%Y-%m-%d",time3))
print(time.strftime('%Y-%m-%d-%H-%M-%S',time3))
print(time.strptime('2018-08-05-21-57-06','%Y-%m-%d-%H-%M-%S'))

datetime.datetime.now()  #获取当前时间
print(datetime.datetime.now()+datetime.timedelta(+3))  #往前或往后时间，