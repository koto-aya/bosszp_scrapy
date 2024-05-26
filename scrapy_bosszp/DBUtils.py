import pymysql

def dbHandle():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="root",
        charset="utf8",
        database="bosszp_db"
    )
    return conn