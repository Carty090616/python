import MySQLdb

# 创建与数据库的连接
conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='111111',db='test',charset='utf8')

# 获取Cursor
cursor = conn.cursor()

cursor.execute("""
create table if not EXISTS user
(
  userid int(11) PRIMARY KEY ,
  username VARCHAR(20)
)
""")
for i in range(1,10):
    cursor.execute("insert into user(userid,username) values('%d','%s')" %(int(i),'name'+str(i)))
conn.commit()


cursor.close()
conn.close()