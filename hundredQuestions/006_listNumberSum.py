# -*- coding:utf-8 -*-
# datetime:2023/1/20 18:45
"""
计算列表数字之和

"""


def listNumberSum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(listNumberSum(list1))
print(listNumberSum(list2))
