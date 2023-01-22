# -*- coding:utf-8 -*-
# datetime:2023/1/22 22:27
"""
输入文件：
    三列：学号，姓名，成绩
    列之间用逗号分割，比如"101,小张,88"
    行之间用\n换行分割
输出：
    最高分、最低分、平均分
"""


def CollectScore(path):
    data_list = []
    with open(path, 'r', encoding='utf-8') as stream:
        for data in stream:
            data = data[:-1]
            new_data = data.split(',')
            score = int(new_data[-1])
            data_list.append(score)
    max_score = max(data_list)
    min_score = min(data_list)
    avg_score = round(sum(score) / len(score), 2)
    return max_score, min_score, avg_score

# def collectScore(data):


path = r'./012_readFile'
print(CollectScore(path))