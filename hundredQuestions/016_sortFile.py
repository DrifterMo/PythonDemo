# -*- coding:utf-8 -*-
# datetime:2023/1/24 17:52
"""
按文件后缀整理文件夹
"""
import os

# def sortFile(path):



path = './arrange_dir'

for file in os.listdir(path):
    file_ext = os.path.splitext(file)[1]
    file_ext = file_ext[1:]
    print(file_ext)