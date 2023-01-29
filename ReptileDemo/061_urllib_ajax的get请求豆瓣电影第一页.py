# -*- coding:utf-8 -*-
# 2023/1/29 16:07
import urllib.request

url = 'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags='

headers = {
    'Accept': 'application/json, text/plain, */*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'bid=meWY1f6_Ir0; douban-fav-remind=1; viewed="26880667"; gr_user_id=fbf9c485-bb7c-4385-bf93-021212bbb654; __gads=ID=1a4ae89a064a3085-227d10ec52d90087:T=1673840831:RT=1673840831:S=ALNI_MbMbrGnPaMY4PVHwAeena3uPpQUyQ; ll="118282"; ap_v=0,6.0; __utma=30149280.1532884915.1673840831.1674038686.1674980994.3; __utmb=30149280.0.10.1674980994; __utmc=30149280; __utmz=30149280.1674980994.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gpi=UID=00000ba53224eeea:T=1673840831:RT=1674981010:S=ALNI_MaQBrdkdx-NSK7rgcrzdR3m7nCEKw',
    'Host': 'm.douban.com',
    'Origin': 'https://movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json
content = json.loads(content)
print(content)