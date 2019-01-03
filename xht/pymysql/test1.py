import pymysql
db = pymysql.connect(
    host="172.16.42.133",port=3306,user="root",passwd="password",db="test")
cursor = db.cursor()
sql = "select * from person"
data=(" ",)
# cursor.execute("select * from person")
# data = cursor.fetchone()
cursor.execute(sql )
for row in cursor.fetchall():
    print( row)
# print('共查找出', cursor.rowcount, '条数据')

print(data)
db.close()