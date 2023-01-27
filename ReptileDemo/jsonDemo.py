fp = open('text.txt', 'w')
# 默认情况 我们只能将字符串写到文件中
fp.write('hello world')
fp.close()

fp = open('text.txt', 'w')
"""
TypeError: write() argument must be str, not list
默认状态下对象是无法写入到文件中  如果想要写入文件，那么必须要使用序列化
"""
name_list = ['zhangsan', 'lisi']
fp.write(name_list)

# 序列化的2中方式
# dumps()
# (1) 创建一个文件
fp = open('text.txt', 'w')

# (2) 定义一个列表
name_list = ['zs', 'ls']

# 导入JSON模块到该文件中
import json

# 序列化
# 将python对象 变成 JSON字符串
# 我们在使用scrapy框架的时候 该框架会返回一个对象  我们要将对象写入文件中 就要使用json.dumps

names = json.dumps(name_list)
# print(names)    # ["zs", "ls"]
# print(type(names))  # <class 'str'>

# 将names写到文件中
fp.write(names)
fp.close()

# # dump()
# # 在将对象转换为字符串的同时，指定一个文件的对象 然后将转换后的字符串写入到这个文件里
fp = open('text.txt', 'w')
name_list = ['z\s', 'list']

import json

# 相当于names = json.dumps(name_list) 和 fp.write(names)
json.dump(name_list, fp)

fp.close()

# 反序列优化
# 将JSON的字符串变成一个python对象

fp = open('text.txt', 'r')
content = fp.read()

# 读取之后 是字符串类型
# print(content)  # ["z\\s", "list"]
# print(type(content))  # <class 'str'>

# loads
import json

# 将JSON字符串变为python对象
result = json.loads(content)
# 转换之后
print(result)  # ['z\\s', 'list']
print(type(result))  # <class 'list'>

# load
fp = open('text.txt', 'r')
import json

result = json.load(fp)
print(result)  # ['z\\s', 'list']
print(type(result))  # <class 'list'>
fp.close()
