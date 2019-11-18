# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:29:23 2019

标签树的下行遍历有3个属性：
.contents    子节点的列表，将<tag>所有儿子节点存入列表；
.children    子节点的迭代类型，与.contents类似，用于循环遍历儿子节点；
下行遍历代码：
for child in soup.body.children
    print(child)    #遍历儿子节点
.descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历；

标签树的上行遍历有2个属性：
.parent    节点的父亲标签；
.parents   节点先辈标签的迭代类型，用于循环遍历先辈节点；
上行遍历代码：
soup = BeautifulSoup(demo, "html.parser")
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        
标签树的平行遍历，bs4一共提供了4个平行遍历属性：
平行遍历是有条件的：要发生在同一个父节点下。
.next.sibling    返回按照html文本顺序的下一个平行节点标签；
.previous_sibling    返回按照html文本顺序的上一个平行节点标签；
.next_siblings    迭代类型，返回按照html文本顺序的后续所有平行节点标签；
.previous_siblings    迭代类型，返回按照html文本顺序的前续所有平行节点标签；

遍历后续标签
for sibling in soup.a.next_siblings:
    print(sibling)
    
遍历前续标签
for sibling in soup.a.previous_siblings:
    print(sibling)
        
@author: XYSM
"""

from bs4 import BeautifulSoup
import requests
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
#print(soup.head)
#print(soup.head.contents)
#print(soup.body.contents)
#print(len(soup.body.contents))
#print(soup.body.contents[3])

#print(soup.title.parent)
#print(soup.html.parent)    #就是自身
#print(soup.a)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        
print(soup.a.next_sibling) # a标签的下一个平行标签是and
print(soup.a.next_sibling.next_sibling) #再下一个平行标签
print(soup.a.previous_sibling) # a标签的前一个标签












































        