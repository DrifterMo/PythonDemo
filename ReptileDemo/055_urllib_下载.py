# -*- coding:utf-8 -*-
# datetime:2023/1/28 16:07


import urllib.request

# 下载网页
url_page = 'http://baidu.com/'
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'https://pic.netbian.com/uploads/allimg/230127/001928-16747499686793.jpg'
urllib.request.urlretrieve(url_img, 'photo.jpg')

# 下载视频
url_video = 'https://vd4.bdstatic.com/mda-ketr0wcivs5kcxq3/v1-cae/sc/mda-ketr0wcivs5kcxq3.mp4?v_from_s=hkapp-haokan-hnb&amp;auth_key=1674895994-0-0-9f3fb23ca1035a3fc454c6282c9e19e4&amp;bcevod_channel=searchbox_feed&amp;pd=1&amp;cd=0&amp;pt=3&amp;logid=1394755568&amp;vid=11176991775839298768&amp;abtest=106991_2&amp;klogid=1394755568'
urllib.request.urlretrieve(url_video, '123.mp4')