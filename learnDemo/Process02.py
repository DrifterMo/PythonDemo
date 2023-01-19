# -*- coding:utf-8 -*-
"""
datetime:2023/1/19 15:22
进程：自定义
"""

from multiprocessing import Process


class MyProcess(Process):

    def __init__(self,name):
        super(MyProcess, self).__init__()
        self.name = name


    # 重写run方法
    def run(self):
        n =1
        while True:
            # print('进程名字' + self.name)
            print('---------->自定义进程, n:{}'.format(n, self.name))
            n += 1

if __name__ == '__main__':
    p = MyProcess('小明')
    p.start()   # 开启新的进程后，或自动调用p.run()

    p1 = MyProcess('小红')
    p1.start()
