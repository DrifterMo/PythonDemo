# -*- coding:utf-8 -*-
# 2023/1/28 18:56

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Acs-Token': '1674893120600_1674960176294_JOcYq0eO+m3w8SFUV5QrP7oi8BQeLPya9oBStyUEzVKO7uFGIf8OSndBXS+Z6rTfZrcEsvigDrNdDyLpftZJcZ7W54VB+09919id8Hspzu6VqnezAtwgcqiFItekx1TgUP4zsC8G0/mdfupOihPpuW0puewxBsvNehdMBY0qTLQR8AW2NW+72pMNtZEl/AHuSyLNoxIXFOOUZwZQKJpZ7z9cKNAW9LS7hZLQTTdpJAc9QYqqJsclPMtvlPiHIjAFCovYXpdZW+rJ6rbhjA05Dbehh0dsa7RfU+Yf5faDZV+QxgARFQEys/y7hg/Yt2Rt',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '136',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=2E33CCA66BF3D0AD87C3749C4825E858; PSTM=1668317140; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=2E33CCA66BF3D0ADFA4F7E413AF679DE:SL=0:NR=10:FG=1; MCITY=-340%3A; BDUSS=JPVEVBbDR-RUFVOHBWa0VmdmNYSnlTTXByVEotVkp1VmtLWGRvVGU2T20tc0JqSVFBQUFBJCQAAAAAAAAAAAEAAAAF9tsvQ27Yr-zhut236L~xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKZtmWOmbZljeU; BDUSS_BFESS=JPVEVBbDR-RUFVOHBWa0VmdmNYSnlTTXByVEotVkp1VmtLWGRvVGU2T20tc0JqSVFBQUFBJCQAAAAAAAAAAAEAAAAF9tsvQ27Yr-zhut236L~xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKZtmWOmbZljeU; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=jz0OJexroG0wg66jc3PfMew16l8y6AjTDYrEOwXPsp3LGJLVc4xjEG0PtfxD-sk-oxHpogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oI-MfIvDqTrP-trf5DCShUFsbncTB2Q-XPoO3KJbM-5hM4-5244IbqtDtjF8ymk82Mbgy4op8P3y0bb2DUA1y4vp553N02TxoUJ2--nssp5eqtnWyb8ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD582e5PVKgTa54cbb4o2WbCQ5f3T8pcN2b5oQT8WjhoIatteMj7u040hJDIBoq0wXpOUWJDkXpJvQnJjt2JxaqRCKKbCEp5jDh3MKnkJQPoRe4ROWTRy0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT0jfn3aQ5rtKRTffjrnhPF3MRTQXP6-hnjy3bRf0KLK2J85VbQEbJtaj47b2HjCaq3Ry6r42-39LPO2hpRjyxv4-T0bM4oxJpOJ5jbRs4OoHR7WO-JvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCD2MI893e; H_PS_PSSID=36550_37555_38051_37989_37919_38040_26350_22158_37881; BA_HECTOR=a48g8l0l8k24018g04aka0qm1htbm8u1k; delPer=0; PSINO=7; ZFY=iz7wRenKsCjZEGUWMx1AXqQaw1nH10QdRPcV:BfF151I:C; BAIDUID_BFESS=2E33CCA66BF3D0ADFA4F7E413AF679DE:SL=0:NR=10:FG=1; BDSFRCVID_BFESS=jz0OJexroG0wg66jc3PfMew16l8y6AjTDYrEOwXPsp3LGJLVc4xjEG0PtfxD-sk-oxHpogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oI-MfIvDqTrP-trf5DCShUFsbncTB2Q-XPoO3KJbM-5hM4-5244IbqtDtjF8ymk82Mbgy4op8P3y0bb2DUA1y4vp553N02TxoUJ2--nssp5eqtnWyb8ebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wD582e5PVKgTa54cbb4o2WbCQ5f3T8pcN2b5oQT8WjhoIatteMj7u040hJDIBoq0wXpOUWJDkXpJvQnJjt2JxaqRCKKbCEp5jDh3MKnkJQPoRe4ROWTRy0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8JT0jfn3aQ5rtKRTffjrnhPF3MRTQXP6-hnjy3bRf0KLK2J85VbQEbJtaj47b2HjCaq3Ry6r42-39LPO2hpRjyxv4-T0bM4oxJpOJ5jbRs4OoHR7WO-JvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCD2MI893e; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673919653,1674026266,1674227931,1674959161; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674960157; ab_sr=1.0.1_Zjc1MTFlNWQ4ZWU1NmJjMjUyM2FmZjY2ZWE0MWMzOTc2MGQyNmRhNTNmMTFmNzU0YzFjMTU5MDJkNDYxNDNjMjUyYWQ0MTE0MGI5MmMyZGY2OThiMzM0N2ZhYjU0ZDA3MTEzMWZjNWZlYjI5ZTRlN2UxNTdmNmViYmNlODI5YjdhYmY0MDlhMWIxMDZjNjQwNjEwYjcwYzMzZTNiYmJjZDQ4MDlhNDI2MTU0NjhkMDg3ZmViNDg1MWEyOWEwOTQ0',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    # 'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'spider',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '63766.268839',
    'token': '784110a2fece71cffd95d21d83746034',
    'domain': 'common',
}

# 请求数据编码
data = urllib.parse.urlencode(data).encode('utf-8')

# 定制化请求
request = urllib.request.Request(url, data, headers)

# 获取响应数据
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json

content = json.loads(content)
print(content)


"""
错误提示信息：UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte

未注释掉 请求头headers中的     'Accept-Language': 'zh-CN,zh;q=0.9',


headers 中的关键信息时 Cookies
"""