# -*- coding:utf-8 -*-
# datetime:2023/1/21 22:07

"""
读取成绩文件排序数据

输入文件：
    三列：学号，姓名，成绩
    列之间用逗号分割，比如"101,小张,88"
    行之间用\n换行分割
处理：
    读取文件，按成绩倒序排列
输出：
    排序后的三列数据
"""


def read_file(path):
    file_data = []
    with open(path, 'r', encoding='utf8') as stream:
        for data in stream:
            data = data[:-1]
            file_data.append(data.split(','))
    return file_data


def sorted_data(data):
    return sorted(data, key=lambda x: x[2])


path = r'./012_readFile'
# print(read_file(path))
print(sorted_data(read_file(path)))