# coding = utf-8
"""
求数字阶乘
"""

def factorial(num):
    sum = 1

    while num != 1 and num != 0:
        sum = sum * num
        num = num -1
    return sum


print(factorial(0))