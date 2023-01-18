# -*- coding:utf-8 -*-
"""
datetime:2023/1/18 11:20
"""
import re

import requests

"""
re模块方法：
    match   从头开始匹配
    search  只匹配一次
    findall 查找所有
    sub(正则表达式, '新内容’, string)   替换     
    split   result = re.split(r'[,:]', 'java:100, python:999')  在字符串中搜索如果遇到:或,就分割
            将分割的内容都保存到列表中
            
基础：
    . 任意字符
    [] 范围
    | 或者
    () 一组
    
量词：
    * ≥0 匹配大于等于0次
    + ≥1
    ? 0或1
    {m}  =m
    {m,} >=0
    {m,n} >=m <=n

预定义：
    \s space  匹配任意空白字符
    \S not space  匹配任意非空字符
    \d digit	匹配任意数字，等价于 [0-9]
    \D not digit
    \w word  [0-9a-zA-Z]
    \W not word  [^0-9a-zA-Z_]
    
分组：
    () -----> group(1)
    
number
    (\w+)(\d*)   -----> 调用：group(1)  group(2)
    引用：
    (\w+)(\d*)    \1    \2   表示引用前面的内容

name(命名）
    (?P<name>\w+)    引用：(?P=name)
"""

# msg = 'aa.py ab.txt kk.png uu.py apyb.txt'
# result = re.findall(r'\w+\.py\b', msg)
# print(result)
#
# msg = '<html><h1>abc</h1></html>'
# result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
# print(result)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
#
#
# def func(temp):
#     num = temp.group()
#     num1 = int(num) + 1
#     return str(num1)
#
# result = re.sub(r'\d+', func, 'java:100, python:999')
# print(result)

# def func(temp):
#     num = temp.group()
#     num1 = int(num) + 1
#     return str(num1)
#
# result = re.sub(r'\d+', func, 'java:100, python:999')
# print(result)
#
# result = re.split(r'[,:]', 'java:100, python:999')
# print(result)


# 爬取图片
msg = '<img class="albumsdetail-item-img" src="https://t7.baidu.com/it/u=3862517085,2815801974&amp;fm=193&amp;f=GIF" style="width: 296px; height: 444px; background-color: rgb(230, 217, 62);">'

result = re.search(r'<img class="albumsdetail-item-img" src="(.+?)"', msg)
print(result.group(1))
path = result.group(1)

with open('test_photo.jpg', 'wb') as wstream:
    wstream.write(requests.get(path).content)