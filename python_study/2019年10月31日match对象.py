# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:32:33 2019

match对象的属性
.string 待匹配的文本
.re 匹配时使用的pattern对象(正则表达式)
.pos 正则表达式搜索文本的开始位置
.endpos 正则表达式搜索文本的结束位置

match对象的方法
.group(0) 获得匹配后的字符串
.start() 匹配字符串在原始字符串的开始位置
.end() 匹配字符串在原始字符串的结束位置
.span() 返回(.start(), .end())

@author: XYSM
"""

import re

match = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
if match:
    print(match.group(0))
    
print(type(match))
print(match.string)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.start(), match.end())
print(match.span())