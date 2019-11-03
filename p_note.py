import pymysql

def con_mysql(host, port, user, pw, mysqlName):
    try:
        #连接数据库
        db = pymysql.connect(host,user,pw,mysqlName,port)

        print("ok")
        #使用cursor()方法创建一个游标对象
        cursor = db.cursor()

    except pymysql.Error:
        print("false")







if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3306
    user = "root"
    pw="root"
    mysqlName = "soho"

    con_mysql(host,port,user,pw,mysqlName)
