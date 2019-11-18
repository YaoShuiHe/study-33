# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:21:17 2019

@author: XYSM
"""

import requests
keyword = "python"

try:
    kv = {'wd':'python'}
    r = requests.get("http://www.baidu.com/s", params = kv)
    print(r.status_code)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
#    print(r.text)
except:
    print("爬取失败")
