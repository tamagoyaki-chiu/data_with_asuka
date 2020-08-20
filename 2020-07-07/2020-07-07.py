import csv
import codecs
import requests
import io
import json
from bs4 import BeautifulSoup

h = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    # "Referer: https://www.taiwan.net.tw/m1.aspx?sNo=0001001",
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
i=0
for page in range(1,3):
    r1=requests.get(
        "https://www.taiwan.net.tw/m1.aspx",headers=h,
        params={"sNo":"0001001","page":page}
    )
    p1=BeautifulSoup(r1.text, "html.parser")
    p2=p1.find_all("div",{"class":"columnBlock-info"})
    for d in p2:
        date=d.find("span",{"class":"date"}).text
        link=d.find("a",{"class":"columnBlock-title","target":"_self"})
        # title=link.text
        # url=link.attrs["href"]
        r2=requests.get(
            "https://www.taiwan.net.tw/"+link.attrs["href"],headers=h
        )
        p3=BeautifulSoup(r2.text, "html.parser")
        d2=p3.find("div",{"class":"content"}).find_all("p")
        with codecs.open("news/"+str(i)+".txt","w","utf8") as f:
            f.write(date+"\r\n")
            f.write(link.text+"\r\n\r\n")
            for d3 in d2:
                f.write(d3.text)
        i+=1
#先抓上層在下層


# p2=p1.find_all("span",{
#     "class":"date"
# })
# for d in p2:
#     print(d.text)


# r1=requests.get(
#     "https://shopping.pchome.com.tw/activity/campaign/C126633626?s_c2_3_0",
#     headers={
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#         "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#         "Cookie":"JSESSIONID=7F4F42558CECC11644EC9888305A4108; _ga=GA1.2.1376330643.1594085831; _gid=GA1.2.1544762363.1594085831; TS01782597=01b1aaba6dbaabf98a0b07dba93ad959ef9b301b795782c9e50cf8b5586794c7176390904b80903e0997102dead92b849fa93b6be7dc2ec2888435747116a5d95745c0782c"
#     }
# )
# r=json.loads(r1.text)

# r=r1.json()
# print(r)

# r1.encoding="utf8"
# f=io.StringIO(r1.text)
# r=list(csv.reader(f))
# for d in r:
#     print(d["Id"], d["BaseCategoryName"], d["Subject"])

#q=ai

# with codecs.open("1.csv", "r", "utf8") as f:
#     r=list(csv.reader(f))
#     for d in r:
#         print(d[0], d[1], d[2])
