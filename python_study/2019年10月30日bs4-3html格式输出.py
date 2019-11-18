# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:25:40 2019

如何让html内容更加友好的显示？
能让人阅读，也让程序更好的阅读。
prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行（加了换行符）.
python3原生支持utf-8


@author: XYSM
"""

from bs4 import BeautifulSoup
import requests
url = "https://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
print(soup.a.prettify())

newsoup = BeautifulSoup("<p>中文</p>","html.parser")
print(newsoup.p.string)
print(newsoup.p.prettify())
