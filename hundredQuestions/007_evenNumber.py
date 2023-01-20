# -*- coding:utf-8 -*-
# datetime:2023/1/20 18:49

"""
计算数字范围内的所有偶数
"""


def is_even(num):
    if num % 2 == 0:
        return True


def evenNumber(start_num, end_num):
    list1 = []
    for i in range(start_num, end_num, 1):
        if is_even(i):
            list1.append(i)
    return list1


print(evenNumber(4, 15))