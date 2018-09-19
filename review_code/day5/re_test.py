# Author:zhang
# -*- coding:utf-8 -*-
import re
'''
正则匹配字符串
. 点默认匹配除\n 换行以外的任何一个字符
+ 匹配前一个字符一次或者多次
$ 整个字符串（string）以什么结尾
^ 以什么开头
？ 匹配前一个字符0次或者1次
{m} 匹配前一个字符m次
{m,n}  匹配m到n次
| 陪陪左边或右的字符
'''
res=re.match('aa','aa33')  #Try to apply the pattern at the start of the string, returninga match object, or None if no match was found
print(res.group())
# re.search()  #匹配所有，有多个时只匹配一个
# re.findall()  #匹配所有，返回所有，没有group方法了


print(re.findall("ZHANG\d",'3ZHANGzmmmmmmmmmmmhangggqiangggggzhangdkqiang3zhangggguuZHANG333'))
