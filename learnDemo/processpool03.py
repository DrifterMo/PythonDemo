# -*- coding:utf-8 -*-
"""
datetime:2023/1/19 15:29

"""
""""
非阻塞式线程池: 全部添加到队列中，立刻返回，并没有等待其他进程执行完毕之后才会结束，但是回调函数是等待任务完成之后才调用
"""
import os
from multiprocessing import Pool
import time

# 非阻塞线程
from random import random

def task(task_name):
    print('开始做任务', task_name)
    start = time.time()
    time.sleep(random() *2)
    end = time.time()
    # print('完成任务: {}! 用时:{}, 进程ID：{}'.format(task_name, end-start, os.getpid()))
    return '完成任务: {}! 用时:{}, 进程ID：{}'.format(task_name, end-start, os.getpid())

containter= []

def callback_func(n):
    # print(n)
    containter.append(n)

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '吃饭', '洗衣服', '散步', '打游戏', '看孩子', '做饭']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,), callback=callback_func)

    pool.close()
    pool.join()

    for c in containter:
        print(c)

    print('OVER!!!!!')

