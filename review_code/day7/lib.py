# Author:zhang
# -*- coding:utf-8 -*-
import  importlib
aa=importlib.import_module("lib1.aa")   #@官方建议用这个
print(aa.C("WANG").name)