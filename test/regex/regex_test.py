# -*- coding: UTF-8 -*-
import re

'''
@Project  easy-post 
@File     regex_test.py
@IDE      PyCharm 
@Author   yida
@Email    949226420@qq.com
@Date     2024/12/17 18:00 
@Desc     使用正则表达式从字符串中提取出指定部分的字符串
'''

# 给定的字符串
strings = [
    "@Component(singleton=True)",
    "@Component(singleton =True)",
    "@Component(singleton = True)",
    "@Component(singleton   = True)",
    "@Component( singleton=True)"
]

# 正则表达式模式
pattern = r'@Component\(\s*singleton\s*=\s*(True|False)\)'

# 提取 singleton 属性的值
for s in strings:
    match = re.search(pattern, s)
    if match:
        value = match.group(1)
        print(f"singleton:{value}")
