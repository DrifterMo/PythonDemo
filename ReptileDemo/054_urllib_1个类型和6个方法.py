# # -*- coding:utf-8 -*-
# # datetime:2023/1/28 13:23
#
# import urllib.request
#
# url = 'http://www.baidu.com'
#
# # 模拟浏览器向服务器发送请求
# response = urllib.request.urlopen(url)
#
# # 1个类型和6个方法
# # response是HTTPResponse的类型
# # print(type(response))   # <class 'http.client.HTTPResponse'>
#
# # # 按照一个字节一个字节的去读
# # content = response.read()
# # print(content)
#
# # # 返回多少个字节
# # content = response.read(5)  # b'<!DOC'
# # print(content)
#
# # # 读取一行
# # content = response.readline()
# # print(content)
#
# # content = response.readlines()
# # print(content)
#
# # # 返回状态码  如果是200了 那么就证明我们的逻辑没有错
# # print(response.getcode())
#
# # # 返回的是url
# # print(response.geturl())
# #
# # # 获取一个状态信息
# # print(response.getheaders())