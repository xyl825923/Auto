# -*- coding: UTF-8 -*-
"""
@Project: Auto
@Author : yuling xiao
@Date : 2023/7/6 9:15
@File : demo.py
@Describe:
    校验接口是否发送成功

"""
import pytest
import requests

from configs.read_conf import read_conf

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "charset": "utf-8",
    "cache-control": "no-cache",
    "Cookie": "authCode=ec58e998cced40158c70f9bcf43f7624; gr_session_id_ab87adcba464486b_67f8e034-7869-4785-8b0e-6b4ca9ad7c63=true; gr_session_id_ab87adcba464486b=67f8e034-7869-4785-8b0e-6b4ca9ad7c63; visitorId=miz1688648879771823136; gr_user_id=50e75274-899a-4850-bdaf-f69b105a2ade; uqKey=22ed286e377b40b1a56ffd1e457ef6f4; ysSession=NjNkOTQ2ZGItNWQxMi00MzhkLWFjODMtMTlmNjUyYmQ0ZGI0; jvm_group=jdy-scm-hz-g0; newOldType=2; userId=10629452; dbId=7968391291488; multiCorp=10629452_hI3mc9OptShvHo6q2+5qsg==; Hm_lvt_8a7c78ab1eac75b2b8ed9c6e7276c083=1688648880; userName=u18722997941; Hm_lpvt_8a7c78ab1eac75b2b8ed9c6e7276c083=1688648880; app-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOnsic2hhcmRLZXkiOiJkYi5zaGFyZDIiLCJ1c2VySWQiOjEwNjI5NDUyfSwiZ3JwIjoibnMtdjMtc2NtLWcwIiwiZXhwIjoxNjg4Njc3Njg1LCJhaWQiOiI3OTY4MzkxMjkxNDg4IiwiaWF0IjoxNjg4NjQ4ODg1fQ.Y9DM4HKaWc8xo1Thipk1GzzXTbmZcnsbQ-_cJU8QTyk; rec_id=1688648879.191610036106",
    "Referer": "https://vip2-hz.jdy.com/"
}

data = {
    "matchCon": "",
    "beginDate": "2023-07-01",
    "endDate": "2023-07-05",
    "_search": False,
    "nd": 1688553599636,
    "rows": 100,
    "page": 1,
    "sord": "asc",
    "billStatus": "",
    "checked": -1
}
session = requests.session()
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "charset": "utf-8",
    "cache-control": "no-cache",
    "Referer": "https://vip2-hz.jdy.com/"
}
headers1['Cookie'] = read_conf('headers', 'cookie')
res = requests.post(url='https://vip2-hz.jdy.com/scm/invPo.do?action=list', headers=headers1, data=data, allow_redirects=False, verify=False)

# res = session.post(url="https://vip2-hz.jdy.com/scm/invPo.do?action=list", headers=headers1, data=data,
#                    allow_redirects=False, verify=False)
print(res.text)
