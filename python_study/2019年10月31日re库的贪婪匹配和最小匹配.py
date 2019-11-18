# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:52:36 2019
re库默认采用贪婪匹配，即输出匹配最长的字串

最小匹配操作符
*? 前一个字符0次或无限次扩展，最小匹配
+? 前一个字符1次或无限次扩展，最小匹配
?? 前一个字符0次或1此扩展，最小匹配
{m,n}? 扩展前一个字符m至n次(含n)，最小匹配

@author: XYSM
"""
# 本例有4个结果
import re
match = re.search(r'PY.*N', 'PYANBNCNDN')
print(match.group(0)) #输出默认匹配

match = re.search(r'PY.*?N', 'PYANBNCNDN') #增加?号
print(match.group(0)) #输出默认匹配