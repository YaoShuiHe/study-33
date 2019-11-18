# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:06:22 2019

信息提取的一般方法：
方法一：完整解析信息的标记形式，再提取关键信息。信息解析准确，过程繁琐，速度慢。
方法二：无视标记形式，直接搜索关键信息。过程间接，速度快，提取结果的准确性有缺点。
方法三：融合方法，结合形式解析与搜索方法，提取关键信息。
以bs4为例，提取HTML总所有的URL链接。
<>.find_all(name, attrs, recursive, string, **kwargs)
方法返回一个列表类型，存储查找的结果。
name:对标签名称的检索字符串。
attrs:对标签属性值的检索字符串，可标注属性检索。
recursive:是否对子孙全部检索，默认True。
string:<>...</>中字符串区域的检索字符串。

由于find_all()函数非常常用，所以有一种简短形式。
<tag>()等价于<tag>.find_all(),即：
soup()等价于soup.find_all()

find_all()还有七个扩展方法。

@author: XYSM
"""

#思路
#1、搜索到所有的<a>标签
#2、解析<a>标签格式，提取href后的链接内容。

from bs4 import BeautifulSoup
import requests

url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

#for link in soup.find_all('a'):
#    print(link.get('href'))
#    
#print(soup.find_all(['a','b'])) #同时找2个标签
#
#for tag in soup.find_all(True):
#    print(tag.name)
    
#只显示以b开头的标签，需要用正则表达式
import re
#for tag in soup.find_all(re.compile('b')):
#    print(tag.name)
    
#查找p标签中包含course字符串的信息
#print(soup.find_all('p', 'course'))
#
#print(soup.find_all(id='link1'))
#
#print(soup.find_all(id='link'))
#
#print(soup.find_all(id=re.compile('link')))
#
#print(soup.find_all(string = "Basic Python"))
#print(soup)
print(soup.find_all(string = re.compile("python")))