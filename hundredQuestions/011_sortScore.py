# -*- coding:utf-8 -*-
# datetime:2023/1/20 23:19
"""
学生成绩排序

学生成绩格式：
    复杂列表，元素是字典或元组
    [
    {'sno': 101, 'sname': '小张', 'sqrade': 88},
    {'sno': 102, 'sname': '小王', 'sqrade': 77},
    {'sno': 103, 'sname': '小李', 'sqrade': 99},
    {'sno': 104, 'sname': '小赵', 'sqrade': 66}
]
可以提供自定义键函数来自定义排序顺序，并且可以设置反转标志以请求按降序排序的结果。
"""
students = [
    {'sno': 101, 'sname': '小张', 'sqrade': 88},
    {'sno': 102, 'sname': '小王', 'sqrade': 77},
    {'sno': 103, 'sname': '小李', 'sqrade': 99},
    {'sno': 104, 'sname': '小赵', 'sqrade': 66}
]

student_sort = sorted(students, key= lambda x:x['sqrade'])
print(student_sort)

