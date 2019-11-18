# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:06:44 2019

@author: XYSM
"""

import requests
url = "https://www.amazon.cn/dp/B00YHL1OKI/ref=lp_1559274071_1_1?s=electronics&ie=UTF8&qid=1572340857&sr=1-1"

try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    print(r.encoding)
    print(r.request.headers)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")