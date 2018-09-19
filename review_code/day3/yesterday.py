# Author:zhang
# -*- coding:utf-8 -*-
import sys
import time
'''
r  是只读
w  是只写，创建并写入，若有源文件，直接覆盖
a  是追加,也不能读
r+ 既能读又能写，写是追加写
w+ 写读，先创建文件再读，只能追加不能seek之后再写入
a+ 追加读？？
python3 中
rb 读二进制二进制文件
wb 写二进制文件
ab 追加二进制文件
readlines 适合读小文件

seek和tell一起使用
with 代码块执行完毕时，内部会自动关闭并释放文件资源，若不关闭文件，会占着内存
python2.7之后支持打开多个文件
with open(file1) as file1,
    open(file) as file2:
'''

# sys.stdout.write("###")    #打印进度条
# for i in range(50):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.5)



f=open('yeterday2','r',encoding='utf-8')
# f.write("wo ai tian an men \n")
# f.write("wo ai tian an men \n")
# f.write("wo ai tian an men \n")
f1=open('yesterday','w',encoding='utf-8')
for line in f:
    if line=='898989898':
        line.replace('898989898','555555555555555555555555555555')
    f1.write(line)

# f.truncate() # 清空文件，不输入参数是直接清空，输入数字，是从数字之后开始清空，

# print(f.tell())
# f.write("qqqqqqqqq")
# f.readline()
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
# print(f.encoding)  #打印文件编码
# print(f.fileno())  #返回文件中句柄的编号，不是内存对象，不用关注
# print(f.name)  #文件名
# f.seekable()  #判断是否能转移

f.flush()  #强制将数据实施刷入硬盘

# f.write('111111111')

#High bige
# count=0
# for line in f:   #效率最高的,f（迭代器）
#     # count+=1
#     if count==9:
#         # count+=1
#         print('qqqqqqqqqq77')
#         break
#     print(line.strip(),'898989')
#     count+=1


#low loop
# for index,i in enumerate(f.readlines()):
#
#     if index==9:
#         print('------',index)
#         continue
#     print(i.strip(),index)