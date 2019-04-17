import pymysql

# 连接
def connect_db():
    return pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='111111',
                           database='test',
                           charset='utf8')

# 插入
def insert(s_name, s_code):
    con = connect_db()
    cur = con.cursor()
    try:
        sql_str = ("INSERT INTO stock_company (s_name, s_code) VALUES ('%s', '%s')" % (s_name, s_code))
        cur.execute(sql_str)
        con.commit()
    except Exception as e:
        con.rollback()
        print(e.message)
        raise
    finally:
        cur.close()
        con.close()