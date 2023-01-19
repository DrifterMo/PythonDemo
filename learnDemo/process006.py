# -*- coding:utf-8 -*-
# datetime:2023/1/19 17:05

# 进程间通信
from multiprocessing import Process, Queue
from time import sleep


def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man,jpg']
    for image in images:
        print("正在下载：", image)
        sleep(0.5)
        q.put(image)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print("{}保存成功".format(file))
        except:
            print("全部保存完毕！")
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))

    p1.start()
    # p1.join()

    p2.start()
    # p2.join()
    print('--------------------------------')

