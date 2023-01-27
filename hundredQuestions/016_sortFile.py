# -*- coding:utf-8 -*-
# datetime:2023/1/24 17:52
"""
按文件后缀整理文件夹
"""
import os
import shutil

# def sortFile(path):



path = './arrange_dir'

for file in os.listdir(path):
    file_ext = os.path.splitext(file)[1]
    file_ext = file_ext[1:]
    if not os.path.isdir(f"{path}/{file_ext}"):
        os.mkdir(f'{path}/{file_ext}')
    source_path = f'{path}/{file}'
    target_path = f'{path}/{file_ext}/{file}'
    shutil.move(source_path, target_path)
    print(file, file_ext)