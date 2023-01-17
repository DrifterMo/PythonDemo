# coding = utf8

"""
time 模块
"""

import time

# 打印时间戳
t = time.time()
print(t)

time.sleep(1)
# 将时间戳转化为字符串
print(time.ctime(t))

# 将时间戳转换为元组
s = time.localtime(t)
print(s)
print(s.tm_hour)

# 元组转回时间戳
print(time.mktime(s))

# 将元组转换为字符串  （默认取当前时间）
s= time.strftime("%Y-%m-%d %H:%M:%S")
print(s)

# 将字符串转换为元组
r = time.strptime('2019/06/20','%Y/%m/%d')
print(r)