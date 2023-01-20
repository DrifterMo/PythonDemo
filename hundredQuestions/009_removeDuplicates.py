# -*- coding:utf-8 -*-
# datetime:2023/1/20 19:07
"""
对列表去重
"""


def removeDuplicates(list):
    new_list = []
    for num in list:
        if num not in new_list:
            new_list.append(num)

    return new_list


list1 = [10, 20, 30, 10, 20]
print(removeDuplicates(list1))