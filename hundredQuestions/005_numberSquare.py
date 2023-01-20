# -*- coding:utf-8 -*-
"""
datetime:2023/1/18 10:56

求前N个数字的平方和
1*1 + 2*2 +3*3 + ...+ n*n
"""

def numberSquare(num):
    sum = 0
    for n in range(1, num+1):
        sum += n*n

    return sum


print(numberSquare(0))