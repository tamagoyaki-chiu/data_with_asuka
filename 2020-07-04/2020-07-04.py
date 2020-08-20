#%%
import requests
import codecs
# r1=requests.get("https://www.ntub.edu.tw/")

# 編碼
# print(r1.status_code)
# 標題
# print(r1.headers)
# 編碼
# print(r1.encoding)
# r1.encoding="utf8"

#print(r1.text)
#print(r1.encoding)

# with codecs.open("1.html","w","utf8") as f:
#     f.write(r1.text)

# r2=requests.get("https://www.ntub.edu.tw/var/file/0/1000/img/159")
# with codecs.open("1.png","wb") as f:
#     f.write(r2.content)

# for p in range(1,4,1):
#     r1=requests.get(
#         "https://tw.kissgoddess.com/people/asuka-saito.html",
#         headers={
#             "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
#         },
#         params={
#             "sNo":"0001001",
#             "page":p
#         }
#     )
#     with codecs.open("html/"+str(p)+".html","w","utf8") as f:
#         f.write(r1.text)

r1=requests.post("https://www.ntub.edu.tw/app/index.php",
    params={
        "Action":"mobileloadmod",
        "Type":"mobile_asso_cg_mstr",
        "Nbr":"1003"
    }
)
print(r1.text)
