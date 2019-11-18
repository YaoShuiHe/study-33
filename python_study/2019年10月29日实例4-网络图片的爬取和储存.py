# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:29:15 2019

@author: XYSM
"""


import requests
import os
url = "https://himg2.huanqiucdn.cn/attachment2010/2019/1029/20191029030858485.jpg"
root = "d://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.makedir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")