# -*- coding:utf-8 -*-
# datetime:2023/1/20 18:53

"""
移除列表中的多个元素
"""


def rmListNumber(list1, list2):
    for item in list2:
        list1.remove(item)
    return list1


list1 = [3, 5, 7, 9, 11, 13]
list2 = [7, 9]
print(rmListNumber(list1, list2))