# Author:zhang
# -*- coding:utf-8 -*-
import configparser

config = configparser.ConfigParser()  # 生成一个对象

print('-----------')
# print(config.options("zhang"))  #返回section的下的option的name
config["key"] = {"hello": "qiang",
                 "world": "china",
                 "height": "1000"}
config["name"] = {"name1": "zhang",
                  "name2": "wang"}
with open('config.ini', 'w') as configfile:  # 写入
    config.write(configfile)
print('-----------')
print(config.read('config.ini'))
print(config.sections())  # 以列表形式返回section节点
print(config.defaults())
print(config["key"]["hello"])  # 读取文件内容
print('-----------')
for key in config["key"]:  # 遍历option节点
    print(key)
print('-----------')
config.remove_section("name")  # 删除之后需要重新写入
with open("config.ini", 'w') as configfile:
    config.write(configfile)
print('-----------')
config.remove_option("key", "hello")  # 删除option节点也需要重新写入
aa = open("config.ini", 'w')
config.write(aa)

config.add_section("add_section")
config["add_section"]={"language":"english",
                       "people":"white"}
