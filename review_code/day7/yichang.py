# Author:zhang
# -*- coding:utf-8 -*-
name=["zhang","wang"]
data={}



try:
    name[6]
    data["zhang"]


except KeyError as e:
    print(e)
except IndexError as e1:
    print("indexerrpt:,",e1)
except Exception as e2:
    print("抓住未知错误")
else:  #这一步是没有错
    print("一切正常")
finally:  #最后都执行
    print("9999999999")

class Zhang(Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    raise Zhang("XIAOQIGNATESTING")  #raise触发
except Zhang as e:
    print(e)