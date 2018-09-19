# Author:zhang
# -*- coding:utf-8 -*-
import shutil  #复制文件

f1= open('file1','r')
f2=open('file2','w')
shutil.copyfileobj(f1,f2)  #copy文件对象

shutil.copy('file1','file2')  #直接输入文件名进行copy
shutil.copymode()

shutil.copystat()  #只是copy了文件的权限

shutil.copy()  #将文件和权限都copy

shutil.copy2()

shutil.copytree()  #递归的取拷贝

shutil.rmtree()  #递归删除

shutil.move()   #移动文件

shutil.make_archive()  #压缩文件