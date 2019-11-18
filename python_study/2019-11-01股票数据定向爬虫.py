# 目标：获取上交所和深交所所有股票的名称和交易信息
# 输出：保存到文件中
# 技术路线：requests-bs4-re
# 候选网站：新浪股票 百度股票
# 选择原则：股票信息静态存在于HTML页面中，非JS代码生成，没有robots协议限制。
# 选取方法：浏览器F12，源代码查看等。
# 选取心态：不要纠结于某一个网站，多找信息源尝试。

# 1 从东方财富网获取股票列表
# 2 根据股票列表逐个到百度股票获取个股信息
# 3 将结果存储到文件

import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    return ""

def getStockList(lst, stockURL)
    return ""

def getStockInfo(lst, stockURL, fpat)
    return ""

def main()
    stock_list_url = 