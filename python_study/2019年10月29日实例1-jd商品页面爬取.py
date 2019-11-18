# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:59:14 2019

@author: XYSM
"""

import requests
url = "https://item.jd.com/1102066.html"
try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
except:
        print("爬取失败")
