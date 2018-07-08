# Author:zhang
# -*- coding:utf-8 -*-
import shutil
import time
f1 = open("本届笔记", encoding='UTF-8')
f2 = open("笔记1", 'w')
# shutil.copyfileobj(f1,f2)  #将一个文件对象里的额内容复制到另一个文件对象里
# shutil.copyfile('本届笔记','笔记')  #参数symlinks直接输入源文件名和目的文件名
# shutil.copystat('本届笔记','笔记')  #仅拷贝权限。内容、组、用户均不变，不能穿件目的文件
shutil.copy('本届笔记', 'dd')  # Copy data and mode bits,
shutil.copytree(r'a',r'newa')  # 递归的copy,目标目录不能存在
time.sleep(2)
shutil.rmtree(r'newa')  #Recursively delete a directory tree递归删除目录

shutil.make_archive('yasuo','zip',r'H:\walker\timetest')  #压缩
