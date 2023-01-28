# -*- coding:utf-8 -*-
# 2023/1/28 18:01

import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制为了解决反爬的第一种手段

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 将周杰伦三个字变成Unicode编码格式
# 我们需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')
url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应数据
content = response.read().decode('utf-8')

# 打印数据
print(content)
