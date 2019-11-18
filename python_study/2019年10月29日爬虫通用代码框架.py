# -*- coding: utf-8 -*-
"""
Spyder Editor

通用代码框架
"""

import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if _name_ == "_main_":
    url = "http://www.baidu.com"
    print(getHTMLText(url))