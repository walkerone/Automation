# Author:zhang
# -*- coding:utf-8 -*-
import os
import time


# os模块是与操作系统交互的一个接口
print(os.getcwd())  # 获取当前路径
print(os.chdir("H://Git"))  # 切换目录
print(os.pardir)  # 返回当前父目录的字符串
os.makedirs("H:\\a\\b\\c")  # 可生成多层递归目录，如果最终目录已经存在则报错
os.removedirs("H:\\a\\b\\c")  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir("H:\\A")  # 生成单级目录；相当于shell中mkdir dirname
os.rmdir("H:\\A")  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir("H:\\"))  # 列出当前目录下的所有文件和目录包括隐藏文件
# print(os.remove())  # 删除一个文件
# os.rename("oldfile", "newfilename")  # 重命名
print(os.sep)  #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.pathsep)  #输出用于分割文件路径的字符串 win下为;,Linux下为: 环境变量的
os.system("dir")  #执行shell命令
print(os.environ)  #输出环境变量
print(os.path.abspath("H:\\walker"))  #返回path的绝对路径
print(os.path.split("H:\\walker"))    #将path分割成目录和文件名二元组返回
print(os.path.dirname(r"H:\walker\readwalker.txt"))  #返回文件的所在目录
print(os.path.basename(r"H:\walker\readwalker.txt"))  #返回文件的文件名，返回path最后的文件名。如何path以／或\结尾，那么就会返回空值

print(os.path.exists(r"H:\walker\readwalker.txt"))  #如果path存在，返回True；如果path不存在，返回False
print(os.path.isdir(r"H:\walker\readwalker.txt"))  #如果path是一个存在的目录，则返回True,否则返回False
print(os.path.isfile(r"H:\walker\readwalker.txt"))  #如果path是一个存在的文件，则返回True,否则返回False
# print(os.path.join())   # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.getsize(r"H:\walker"))   #返回一个文件的大小或者一个目录下所有文件的大小
print('[%-15s]' % '#')
print('[%-15s]' %'##')
print('[%-15s]' %'###')
print('[%-15s]' % '####')

print(('[%%-%ds]' % 50) % '##')

