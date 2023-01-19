# -*- coding:utf-8 -*-

"""
datetime:2023/1/19 16:17

"""
"""
阻塞式 : 添加一个执行一个任务，如果一个任务不结束 另一个任务就进不来

进程池：
pool = Pool(max)    创建进程池对象
pool.apply()    阻塞的
pool.apply_async()  非阻塞

pool.close()    停止添加进程
pool.join() 让主进程让步
"""

import os
import time
from multiprocessing import Pool
from random import random


def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    time.sleep(random() *2)
    end = time.time()
    print('完成任务: {}! 用时:{}, 进程ID：{}'.format(task_name, end-start, os.getpid()))
    # return '完成任务: {}! 用时:{}, 进程ID：{}'.format(task_name, end-start, os.getpid())



if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '散步', '打游戏', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply(task, args=(task1,))

    pool.close()
    pool.join()

    print('Over!!!!')