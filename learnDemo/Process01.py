# -*- coding:utf-8 -*-
"""
datetime:2023/1/19 15:00
进程
"""
import os
from time import sleep
from multiprocessing import Process

m = 1   #不可变类型
list1 = []  # 可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task1')
        print("这是任务1.。。。。。。。", m, list1, os.getpid(), '---------------', os.getppid())

def task2(s, name):
    global m
    while True:
        sleep(s)
        m +=1
        list1.append(str(m) + 'task2')
        print("这是任务2.。。。。。。。", m, list1, os.getpid(), '---------------', os.getppid())




if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p1 = Process(target=task1, name="任务1", args=(1, 'aa'))
    p1.start()

    p2 = Process(target=task2, name='任务2', args=(2, 'bb'))
    p2.start()

    while True:
        sleep(1)
        m += 1
        print('------------> main', m)

    # print('---------------------------------')
    # print('*********************************')