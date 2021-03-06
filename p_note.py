import pymysql
import re
import os
import sys


class p_note_mysql():

    def __init__(self,host, port, user, pw, mysqlName, my_table):
            self.host = host
            self.port = port
            self.user = user
            self.pw=pw
            self.mysqlName = mysqlName
            self.my_table=my_table


    def con_mysql(self,host, port, user, pw, mysqlName):
        try:
            #连接数据库
            db = pymysql.connect(host, user, pw, mysqlName, port)
            print("mysql connect.....ok")
            return db

        except pymysql.Error:
            print("mysql connect.....false")
            os._exit(0)



    def cre_cursor(self,db):
        cursor = db.cursor()


        return cursor



    def is_mydb(self,cursor, my_table):
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



    def cre_mydb(self,cursor, my_table):
        print("wait...")
        os.system("pause")
        cursor.execute("CREATE TABLE p_test (name VARCHAR(255), address VARCHAR(255))")
        self.is_mydb(cursor, my_table)


    def clo_mydb(self,cursor,db):
        cursor.close()
        db.close()

        print("end....")

    def cre_field_mydb(self, cursor, p_table, p_field):
        mysql_ord="describe "+p_table+" "+p_field
        if cursor.execute(mysql_ord):
            print("field ....ok")
        else:
            print("field...false")
            os.system("pause")
            cre_field_ord="ALTER TABLE "+p_table+" "+"ADD COLUMN "+p_field+" INT(20)"
            cursor.execute(cre_field_ord)
            print("ok")

    def insert_db(self, cursor, p_table, p_field):
        for i in range(1001):
            insert_ord="insert into %s(%s) values(%d)"%(p_table,p_field,i)
            cursor.execute(insert_ord)
            print("insert ...ok")




if __name__ == "__main__":
    my_test = p_note_mysql(
                             "127.0.0.1",
                             3306,
                             "root",
                             "root",
                             "soho",
                             "p_test"
                             )
    my_db_state = my_test.con_mysql(my_test.host, my_test.port, my_test.user, my_test.pw, my_test.mysqlName)
    my_db_cursor=my_test.cre_cursor(my_db_state)
    if my_test.is_mydb(my_db_cursor, my_test.my_table) == False:
        my_test.cre_mydb(my_db_cursor, my_test.my_table)
    os.system("pause")
    my_test.cre_field_mydb(my_db_cursor, my_test.my_table, "f_test")
    #my_test.insert_db(my_db_cursor,my_test.my_table,"f_test")
    my_test.clo_mydb(my_db_cursor,my_db_state)
