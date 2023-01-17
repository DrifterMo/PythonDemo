# coding = utf-8

"""
输入半径，求圆的面积
"""
import math

def area(radius):
    return round(math.pi * radius * radius, 2)


print(area(2))