# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:16:58 2019

re库是python的标准库，主要用于字符串匹配。
import re
使用raw string类型(原生字符串类型)标识正则表达式
表示为：r'text'
例如：r'[1-9]\d{5}'
原生字符串是不包含转义符的字符串.

re库主要功能函数
re.search(pattern, string, flags=0)   
在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象；
    pattern:正则表达式的字符串或原生字符串表示，
    string：待匹配字符串，
    flags：正则表达式使用时的控制标记，
        re.I re.IGNORECASE 忽略正则表达式的大小写，[A-Z]能够匹配大小写字符
        re.M re.MULTILINE 正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
        re.S re.DOTALL 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符

re.match(pattern, string, flags=0)    
从一个字符串的开始位置起匹配正则表达式，返回match对象；


re.findall(pattern, string, flags=0)  
搜索字符串，以列表类型返回全部能匹配的子串；

re.split(pattern, string, maxsplit=0, flags=0)    
将一个字符串按照正则表达式匹配结果进行分割，返回列表类型；
    maxsplit:最大分割数，剩余部分作为最后一个元素输出，


re.finditer(pattern, string, flags=0)  
搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象；

re.sub(pattern, repl, string, count=0, flags=0)    
在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串；
    repl:替换匹配字符串的字符串，
    count:匹配的最大替换次数，
以上6个函数非常常用

函数式用法：一次性操作
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
面向对象用法：编译后多次操作
pat = re.compile(r'[1-9]\d{5}')
ls = pat.search('BIT100081 TSU100084')

regex = re.compile(pttern, flags=0)
将正则表达式的字符串形式编译成正则表达式对象
    pattern:正则表达式的字符串或原生字符串表示，
    flags:正则表达式使用时的控制标记，
re库的另一种等价用法
regex.search()
regex.match()
regex.findall()
regex.split()
regex.finditer()
regex.sub()




@author: XYSM
"""
# 实例一
import re

#match = re.search(r'[1-9]\d{5}', 'BIT 100081')
#if match:
#    print(match.group(0))
    
# 实例二
#match = re.match(r'[1-9]\d{5}', '100081 BIT')
#if match:
#    print(match.group(0))

# 实例三
#ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
#print(ls)

# 实例四
#ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
#print(ls)       #将匹配的内容删除后输出剩余内容

# 实例五
#for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#    if m:
#        print(m.group(0))

sub = re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
print(sub)
        
