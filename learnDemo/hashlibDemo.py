# coding = utf-8

import hashlib

# msg = 'nihao'
# md5 = hashlib.md5(msg.encode('utf-8'))
# print(md5.hexdigest())

def jm_md5(msg):
    m = hashlib.md5()   # 构建MD5对象
    m.update(msg.encode('utf-8'))   # 设置编码格式 并将字符串添加到MD5对象中
    msg_md5 = m.hexdigest() # hexdigest()将加密字符串生成十六进制数据字符串值
    return msg, msg_md5

msg = jm_md5('Drifter')
print(msg)