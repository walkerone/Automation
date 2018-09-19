# Author:zhang
# -*- coding:utf-8 -*-
import json
import pickle
def savhi():
    print("kkkkkkk")
dict1={'name':'wang','age':'22'}
dict2={'name':'wang','age':'24'}
with open('file.txt','wb') as f:
    # dict1=json.dumps(dict1)
    # f.write(dict1)
    # print(dict1)
    dict2=pickle.dump(dict2,f)   #dump 用法

   #dump用法

    # data=f.read()
    # print(data["name"])