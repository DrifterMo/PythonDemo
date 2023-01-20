# -*- coding:utf-8 -*-
# datetime:2023/1/20 20:56
"""
对简单列表进行排序
简单列表：元素类型不是符合类型（列表/元组/字典）
形式1：[20,50,10,40,30]
形式2：['bb', 'ee', 'aa', 'dd', 'cc']

怎么原地排序？怎么不改变原列表排序？
怎么指定是升序还是降序？
"""
"""
list.sort() 直接对原列表进行修改，直接输出原list

new_list = sorted(list) 不改变原list，将排序结果返回给new_list
"""

list1 = [20, 50, 10, 40, 30]
new_list1 = sorted(list1)
print('不改变原列表排序：', new_list1, "，原列表为：", list1)

list1.sort()
print("升序排序后的列表为：", list1)

list1.sort(reverse=True)
print("降序排序后的列表为：", list1)


list2 = ['bb', 'ee', 'aa', 'dd', 'cc']
new_list2 = sorted(list2)
print('不改变原列表排序：', new_list2, "，原列表为：", list2)

list2.sort()
print("升序排序后的列表为：", list2)

list2.sort(reverse=True)
print("降序排序后的列表为：", list2)
