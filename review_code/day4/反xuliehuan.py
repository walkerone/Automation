# Author:zhang
# -*- coding:utf-8 -*-
import json
import pickle
def savhi():
    print("kkkkkkk")
dict1={'name':'age','age':'22'}
with open('file.txt','rb') as f:
    # data=f.read()
    data1=pickle.load(f)

    print(data1)
