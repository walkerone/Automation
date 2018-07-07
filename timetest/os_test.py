# Author:zhang
# -*- coding:utf-8 -*-
import os
import time
#os模块是与操作系统交互的一个接口
print(os.getcwd()) #获取当前路径
print(os.chdir("h://walker")) #切换目录
print(os.pardir)  #返回当前父目录的字符串
os.makedirs("H:\\a\\b\\c") #可生成多层递归目录，如果最终目录已经存在则报错
time.sleep(10)
os.removedirs("H:\\a\\b\\c") #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir("H:\\A")  #生成单级目录；相当于shell中mkdir dirname
os.rmdir("H:\\A")  #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
