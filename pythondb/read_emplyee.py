import pymysql.cursors
from utilsz import *
connection = utilsz.connectdb.getConnection()
try:
    cursor=connection.cursor()
    sql = "SELECT * FROM employee "
    cursor.execute(sql)
    for i in cursor:
       print(i)
except pymysql.Error as e:
    print("Error %s"% e.args[1])
finally:
    connection.close()