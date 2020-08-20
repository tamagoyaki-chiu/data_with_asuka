#%%
import pymysql

e=pymysql.connect(
	host="localhost",
	user="root",
	passwd=input("請輸入資料庫root密碼:"),
	db="python_ai",
	charset="utf8",
	#port=int(input("請輸入資料庫的Port:")) #額外的port 額外的參數
    )

c=e.cursor()

c.execute("SELECT `a`.*,`b`.`tel` FROM `member`AS`a` INNER JOIN `tel`AS`b` ON `a`.`id`=`b`.`member_id`")


r=c.fetchall()
for d in r:
	print(d[0:])


e.close()

# 抓全部
# SELECT `a`.*,`b`.`tel` FROM
#     `memeber` AS `a` INNER JOIN `tel` AS `b`
#     ON `a`.`id`=`b`.`member_id`

# 以左邊為準
# SELECT `a`.*,`b`.`tel` FROM
#     `memeber` AS `a` LEFT JOIN `tel` AS `b`
#     ON `a`.`id`=`b`.`member_id`

# 以右邊為準的
# SELECT `a`.*,`b`.`tel` FROM
#     `tel` AS `b` RIGHT JOIN `member` AS `a`
#     ON `a`.`id`=`b`.`member_id`

# 抓member的
# SELECT `a`.*,`b`.`tel` format
#     `member` AS `a` RIGHT JOIN `tel` AS `b`
#     ON `a`.`id`=`b`.`member_id`

# 每跑一次記一次
# UPDATE `news` SET `look`=`look`+1 WHERE `id`=  


# %%
