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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36 ",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "charset": "utf-8",
    "cache-control": "no-cache",
    "Cookie": "visitorId=utd1684906763138873235; uqKey=ca2df6905ba84b6f940a15db4f564a36; gr_user_id=90c7d996-38dd-4d8d-96a9-861141faadeb; jvm_group=jdy-scm-hz-g0; newOldType=2; _ati=2090980882524; rec_id=1687939573.254999164; Hm_lvt_8a7c78ab1eac75b2b8ed9c6e7276c083=; Hm_lpvt_8a7c78ab1eac75b2b8ed9c6e7276c083=1688606302; multiCorp=10629452_hI3mc9OptShvHo6q2+5qsg==; userId=10629452; userName=u18722997941; gr_session_id_ab87adcba464486b=fce80c3e-d0a0-4727-9c7c-b4284934097d; gr_session_id_ab87adcba464486b_fce80c3e-d0a0-4727-9c7c-b4284934097d=true; app-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHQiOnsic2hhcmRLZXkiOiJkYi5zaGFyZDIiLCJ1c2VySWQiOjEwNjI5NDUyfSwiZ3JwIjoibnMtdjMtc2NtLWcwIiwiZXhwIjoxNjg4NjM1MTE1LCJhaWQiOiI3OTY4MzkxMjkxNDg4IiwiaWF0IjoxNjg4NjA2MzE1fQ.1mM7n-RJLZz4XHhu5bbGY9kqPzG8hX-V8u_qKPR79IA; authCode=ae8269c44dcf426da10f6edac7ca5160; dbId=7968391291488; ysSession=ZjYwOTJhMjgtMzU5Yi00OTBlLWI5ZmMtYzgyZjkwOWU1M2Uy",
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
res = session.post(url="https://vip2-hz.jdy.com/scm/invPo.do?action=list", headers=headers, data=data,
                   allow_redirects=False, verify=False)
print(res.text)

