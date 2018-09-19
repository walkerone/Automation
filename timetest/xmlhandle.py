# Author:zhang
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
tree=ET.parse("xmltest.xml")
root=tree.getroot()
print(root.tag)
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib,i.text)

print("-------")
#只遍历某一个节点
for node in root.iter("property"):
    print(node.tag,node.attrib)

