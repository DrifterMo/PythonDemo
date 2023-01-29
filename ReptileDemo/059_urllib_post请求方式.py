# -*- coding:utf-8 -*-
# 2023/1/28 18:56
import json
import urllib.parse
import urllib.request

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post请求参数  必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')


# post的请求的参数是不会拼接在url后面的， 而是需要放在请求对象定制的参数中
# post请求的参数 必须进行编码
request = urllib.request.Request(url, data, headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')
print(content)
print(type(content))

# 字符串---->json对象
content = json.loads(content)
print(content)
print(type(content))

# post请求方式的参数 必须编码
# 编码之后 必须调用encode方法
# 参数是放在请求对象定制的方法中

