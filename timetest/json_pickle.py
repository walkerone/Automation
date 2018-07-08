# Author:zhang
# -*- coding:utf-8 -*-
import json
import pickle

"""json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错，
因此在将数据写入时需要用到该函数.json.loads()用于将str类型的数据转成dict。"""

name_emb = {'a': True, 'A': '1111', 'b': '2222', 'c': '3333', 'd': '4444'}
print(name_emb)
print(type(name_emb))
jsobj = json.dumps(name_emb)
json.dump()
print(jsobj)
print(type(jsobj))
