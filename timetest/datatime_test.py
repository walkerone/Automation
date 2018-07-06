#! -*- coding:utf-8 -*-
import datetime
import time
print(datetime.datetime.now())
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))
print(datetime.datetime.now()+datetime.timedelta(hours=5,minutes=1))

