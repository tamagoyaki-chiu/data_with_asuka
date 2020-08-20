import pymysql

e=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="2020-06-30",
	charset="utf8"
)

c=e.cursor()

# c.execute(
# "INSERT INTO `news`(`title`,`source`,`create_time`,`description`)"+
# " VALUES(%(a)s,%(b)s,%(c)s,%(d)s)"
# , {
# 	"c":input("create time:"),
# 	"a":input("title:"),
# 	"b":input("source:"),
# 	"d":input("description:")
# })
# e.commit()

# c.execute(
# "DELETE FROM `news` WHERE `id`=%s"
# , [
# 	input("id:")
# ])
# e.commit()

c.execute("SELECT * FROM `news`")

# d=c.fetchone()
# print(d[0],d[1],d[2])

# d=c.fetchone()
# print(d[0],d[1],d[2])

# d=c.fetchone()
# print(d[0],d[1],d[2])

# r=c.fetchall()
# for d in r:
# 	print(d[0],d[1],d[2])

print(c.rowcount)


e.close()
