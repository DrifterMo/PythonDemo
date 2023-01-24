# -*- coding:utf-8 -*-
# datetime:2023/1/23 21:58

"""
统计目录下文件大小
"""
import os


def collectFileSize(path):
    sum = 0
    if os.path.isfile(path):
        sum = os.path.getsize(path)
    else:
        for file in os.listdir(path):
            new_path = os.path.join(path, file)
            sum += os.path.getsize(new_path)
    return sum


if __name__ == '__main__':
    path = r'./014_englishBook'

    print(collectFileSize(path))