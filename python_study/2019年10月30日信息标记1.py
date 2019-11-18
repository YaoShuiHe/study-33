# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:37:06 2019

信息标记的三种方式：
XML：基于HTML发展的一种表达方式；
    用一对尖括号来表达,有效信息的比例不多，大多数是标签。
    
    <person>
        <firstName>Tian</firstName>
        <lastName>Song</lastName>
        <address>
            <streetAddr>中关村南大街5号</streetAddr>
            <city>北京市</city>
            <zipcode>100081</zipcode>
        </address>
        <prof>Computer System</prof><prof>Security</prof>
    </person>
    最早的通用信息标记语言，可扩展性好，但繁琐。
    现今常用于internet上的信息交互与传递。
json：有类型的键值对key:value
    "key":"value"
    "key":["value1,"value2"]
    "key":{"subkey":"subvalue"}
    
    {
         “firstName":"Tian",
         "lastName":"Song",
         "address:{
                     "streetAddr":"中关村南大街5号",
                     "city":"北京市",
                     "zipcode":"100081"
                 },
         "prof":["Computer System","Security"]
    }
     信息有类型，适合程序处理，较xml简洁。
     主要在移动应用云端和节点的信息通信，无注释。   
YAML:无类型的键值对来组织信息key:value
    name:北京理工大学
    利用缩进来表示所属关系，用“-”来表示并列关系，用竖线表示整块数据。
    
         firstName:Tian
         lastName:"Song
         address:
                 streetAddr:中关村南大街5号
                 city:北京市
                 zipcode:100081
                 
         prof:
             -Computer System
             -Security
        信息无类型，文本信息比例最高，可读性好。
        各类系统的配置文件，有注释易读。
        
@author: XYSM
"""








