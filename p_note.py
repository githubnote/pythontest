import pymysql
import re
import os

def con_mysql(host, port, user, pw, mysqlName):
    try:
        #连接数据库
        db = pymysql.connect(host,user,pw,mysqlName,port)

        print( mysqlName ,"connect ....ok")
        #使用cursor()方法创建一个游标对象
        cursor = db.cursor()

    except pymysql.Error:
        print("false")

    return cursor

def is_mydb(cursor, my_table):
    sql = "show tables;"
    cursor.execute(sql)
    tables = [cursor.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if my_table in table_list:
        print("%s is ok.... " % my_table)
        return True
    else:
        print("%s is no.... " % my_table)
        return False



def cre_mydb(cursor, my_table):
    print("wait...")
    cursor.execute("CREATE TABLE p_test (name VARCHAR(255), address VARCHAR(255))")
    is_mydb(cursor,my_table)







if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3306
    user = "root"
    pw="root"
    mysqlName = "soho"
    my_table="p_test"


    cursor=con_mysql(host,port,user,pw,mysqlName)
    is_mydb(cursor, my_table)
    os.system("pause")
    cre_mydb(cursor,my_table)