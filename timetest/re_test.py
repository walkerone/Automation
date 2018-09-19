# Author:zhang
# -*- coding:utf-8 -*-
# https://www.cnblogs.com/zjltt/p/6955965.html
import re

a1 = re.findall("匹配规则", "要匹配规则的匹配规则字符串")  # 第二步，调用模块函数
print(a1)
# ^ 元字符 字符串开始位置与匹配规则符合就匹配，否则不匹配
# 匹配字符串开头。在多行模式中匹配每一行的开头
# ^元字符如果写到[]字符集里就是反取
a = re.findall("^匹配规则", "匹配规则这个字符串是否匹配")  # 字符串开始位置与匹配规则符合就匹配，否则不匹
print(a)
# [^a-z]反取，匹配出除字母外的字符，^元字符如果写到字符集里就是反取
a = re.findall("[^a-z]", "匹配s规则这s个字符串是否s匹配f规则则re则则则")
print(a)

'''
$元字符字符串结束位置与匹配规则符合就匹配，否则不匹配
匹配字符串末尾，在多行模式中匹配每一行的末尾'''
a = re.findall("匹配规则$", "快乐撒大家ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff匹配规则"
                        "ff匹配规则")
print(a)

'''
*元字符需要字符串里完全符合，匹配规则，就匹配，（规则里的*元字符）前面的一个字符可以是0个或多个原本字符
匹配前一个字符0或多次，贪婪匹配前导字符有多少个就匹配多少个很贪婪
如果规则里只有一个分组，尽量避免用*否则会有可能匹配出空字符串'''
a = re.findall("匹配规则 *", "这个字符串是否匹配规则   则则则则")  # 需要字符串里完全符合，匹配规则，就匹配，（规则里的*元字符）前面的一个字符可以是0或多个原本字符
print(a)

'''
+元字符需要字符串里完全符合，匹配规则，就匹配，（规则里的+元字符）前面的一个字符可以是1个或多个原本字符
匹配前一个字符1次或无限次，贪婪匹配前导字符有多少个就匹配多少个很贪婪'''
a = re.findall("匹配+", "匹配配配配配规则这个字符串是否匹配规则则则则则")  # 需要字符串里完全符合，匹配规则，就匹配，（规则里的+元字符）前面的一个字符可以是1个
print(a)

'''
?元字符，和防止贪婪匹配
需要字符串里完全符合，匹配规则，就匹配，（规则里的?元字符）前面的一个字符可以是0个或1个原本字符
匹配一个字符0次或1次
还有一个功能是可以防止贪婪匹配，详情见防贪婪匹配'''
a = re.findall("匹配规则?", "匹配规这个字符串是否匹配规则则则则则")  # 需要字符串里完全符合，匹配规则，就匹配，（规则里的?元字符）前面的一个字符可以是0个或1个
print(a)
'''
{}元字符,范围
需要字符串里完全符合，匹配规则，就匹配，（规则里的 {} 元字符）前面的一个字符，是自定义字符数，位数的原本字符
{m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至无限次
{0,}匹配前一个字符0或多次,等同于*元字符
{+,}匹配前一个字符1次或无限次,等同于+元字符
{0,1}匹配前一个字符0次或1次,等同于?元字符'''
a = re.findall("匹配规则{3}", "匹配规这个字符串是否匹配规则则则则则")  # {m}匹配前一个字符m次，{m,n}匹配前一个字符m至n次，若省略n，则匹配m至
print(a)
'''
[]元字符,字符集
需要字符串里完全符合，匹配规则，就匹配，（规则里的 [] 元字符）对应位置是[]里的任意一个字符就匹配
字符集。对应的位置可以是字符集中任意字符。字符集中的字符可以逐个列出，也可以给出范围，如[abc]或[a-c]。[^abc]表示取反，即非abc。
所有特殊字符在字符集中都失去其原有的特殊含义。用\反斜杠转义恢复特殊字符的特殊含义。'''
a = re.findall("匹配[a,b,c]规则", "匹配a规则这个字符串是否匹配b规则则则则则")   #需要字符串里完全符合，匹配规则，就匹配，（规则里的 [] 元字符）对应位置是[]里的任意一个字符就匹配
print(a)

#^]非，反取，匹配出除[^]里面的字符，^元字符如果写到字符集里就是反取
a = re.findall("[^a-z]", "匹配s规则这s个字符串是否s匹配f规则则re则则则")   #反取，匹配出除字母外的字符
print(a)
'''
反斜杠后边跟普通字符实现特殊功能；（即预定义字符）
预定义字符是在字符集和组里都是有用的
\d匹配任何十进制数，它相当于类[0-9]'''
a = re.findall("\d", "匹配规则这2个字符串3是否匹配规则5则则则7则")   #\d匹配任何十进制数，它相当于类[0-9]
print(a)
#\d+如果需要匹配一位或者多位数的数字时用
a = re.findall("\d", "匹配规则这2个字符串3是否匹配规则5则则则73333fffffffff则")   #\d匹配任何十进制数，它相当于类[0-9]
print(a)

#\D匹配任何非数字字符，它相当于类[^0-9]
a = re.findall("\d+", "匹配规则这2个字符串134444是否匹配规ddd3333则5则则则7则")   #\d+如果需要匹配一位或者多位数的数字时用
print(a)  #以列表形式返回匹配到的字符串

#\D匹配任何非数字字符，它相当于类[^0-9]
a = re.findall("\D", "匹配规则这2个字44符串3是否匹小强配规则5则则则7则")   #\D匹配任何非数字字符，它相当于类[^0-9]
print(a)  #以列表形式返回匹配到的字符串

#\s匹配任何空白字符，它相当于类[\t\n\r\f\v]
a = re.findall("\s", "匹配规则   这2个字符串3是否匹\n配规则5则则则7则")   #\s匹配任何空白字符，它相当于类[\t\n\r\f\v]
print(a)  #以列表形式返回匹配到的字符串

#|元字符，或 |或，或就是前后其中一个符合就匹配
#()元字符，分组
a = re.findall(r"你|好", "a4a4a你4aabc4a4dgg好dg4g654g")   #|或，或就是前后其中一个符合就匹配
print(a)

'''也就是分组匹配，()里面的为一个组也可以理解成一个整体
如果()后面跟的是特殊元字符如   (adc)*   那么*控制的前导字符就是()里的整体内容，不再是前导一个字符'''
a = re.search("(a4)+", "a4a4a4a4a4dg4g654gb")   #匹配一个或多个a4
print(a)
'''match，从头匹配一个符合规则的字符串，从起始位置开始匹配，匹配成功返回一个对象，未匹配成功返回None
match(pattern, string, flags=0)
# pattern： 正则模型
# string ： 要匹配的字符串
# falgs ： 匹配模式
注意：match()函数 与 search()函数基本是一样的功能，不一样的就是match()匹配字符串开始位置的一个符合规则的字符串，search()是在字符串全局匹配第一个合规则的字符串'''
