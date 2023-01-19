# -*- coding:utf-8 -*-
# datetime:2023/1/19 16:47
#
"""
进程间的通信
"""
from multiprocessing import Queue
q = Queue(5)

q.put('A')
q.put('B')
q.put('C')
q.put('D')
q.put('E')
print(q.qsize())
if not q.full():    # 判断队列是否满   q.empty() 判断队列是否为空
    q.put('F', timeout=2)   # put() 如果queue满了则只能等待，除非有’空地‘则添加成功
else:
    print("队列已满！")

# 获取队列的值
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))
print(q.get(timeout=2))

q.put_nowait()
q.get_nowait()