# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:58:02 2019

BeautifulSoup类有五种基本元素：
tag    标签，最基本的信息组织单元，分辨用<>和</>标明开头和结尾；
name   标签的名字，<p>...</p>的名字是p，格式：<tag>.name;
attributes    标签的属性，字典形式组织，格式：<tag>.attrs;
navigablestring    标签内非属性字符串，<>...</>中字符串，格式：<tag>.string;
comment    标签内字符串的注释部分，一种特殊的comment类型;

@author: XYSM
"""
from bs4 import BeautifulSoup
import requests
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
#print(demo)
soup = BeautifulSoup(demo, "html.parser")
#print(soup.title)
tag = soup.a
print(tag)

print(soup.a.name)
#print(soup.a.parent.name)
#print(soup.a.parent.parent.name)
#
#tag = soup.a
#print(tag.attrs)
#print(tag.attrs['class'])
#print(tag.attrs['href'])

#print(type(tag.attrs))
#print(type(tag))
#
#print(soup.a.string)
#print(soup.p.string)
#print(type(soup.p.string))
#
#newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
#print(newsoup.b.string)
#print(type(newsoup.b.string))
#print(newsoup.p.string)
#print(type(newsoup.p.string))