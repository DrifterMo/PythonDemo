# -*- coding:utf-8 -*-
# datetime:2023/1/23 16:52
"""
统计一篇英文文章中出现最多的单词
"""

dict = {}
with open('./014_englishBook', 'r', encoding='utf8') as stream:
    for data in stream:
        data = data[:-1]    # 去掉换行符\n
        words = data.split()    # 按空格分割
        for word in words:
            if word not in dict:
                dict[word] = 1
            dict[word] += 1

print(
    sorted(
    dict.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]
)
# print(dict.items())
