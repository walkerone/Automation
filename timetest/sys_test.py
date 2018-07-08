# Author:zhang
# -*- coding:utf-8 -*-
import sys
import time
print(sys.argv[0])  #命令行参数List，第一个元素是程序本身路径,需要在命令执行
# print(sys.argv[1])
n=0
sys.exit(n)  #退出程序，正常退出时exit(0),其它是异常退出
def progress(percent,width=50):
    if percent >= 1:
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
    print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')

progress(0.5)