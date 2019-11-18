# scrapy是个功能强大的网络爬虫框架，是一个基于python的第三方库
# pip install scrapy
# scrapy -h测试安装成功否
# scrapy不是一个函数功能库，二十一个爬虫框架
# 爬虫框架是实现爬虫功能的一个软件结构和功能组件集合
# 爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫
# scrapy爬虫框架一共包含7个部分，5+2结构，5个是框架的主体部分，2个中间件
# 5个是：engine、scheduler、item pipelines、spiders、downloader模块
# 2个是：engine和spiders之间的中间件、engine和downloader之间的中间件
# engine、downloader、scheduler模块是已有实现的
# spiders、item pipelines要用户编写

# engine和downloader之间的中间件 downloader middleware
#   目的：实施engine、scheduler、和downloader之间进行用户可配置的控制
#   功能：修改、丢弃、新增请求或响应
# requests vs. scrapy
# 相同点：两者都可以进行页面请求和爬取，python爬虫的两个重要技术路线
#        两者可用性都好，文档丰富，入门简单
#        两者都没有处理js、提交表单、应对验证码等功能(可扩展)
# 不同点：  requests            scrapy
#           页面级爬虫          网站级爬虫
#           功能库              框架
#           并行性考虑不足      并发性好，性能较高
#           重点在于页面下载    重点在于爬虫结构
#           定制灵活            一般定制灵活，深度定制困难
#           上手十分简单        入门较难
# scrapy命令行格式：
# >scrapy <command> [options] [args]
# scrapy常用命令6个
# startproject 创建一个新工程 scrapy startproject <name> [dir]
# genspider 创建一个爬虫 scrapy genspider [options] <name> <domain>
# settings 获得爬虫配置信息
# crawl 运行一个爬虫
# list 列出工程中的所有爬虫
# shell 启动url调试命令行
