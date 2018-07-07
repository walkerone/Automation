#! -*- coding:utf-8 -*-
import datetime
import time
print(datetime.datetime.now())  #获取当前时间
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.now()+datetime.timedelta(3))  #获取几天前的时间，timedelta不能独立存在，
# 必须和datatime函数一起使用
print(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=1,seconds=8))

