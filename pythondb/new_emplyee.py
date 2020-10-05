import pymysql.cursors
from utilsz import *
connection = utilsz.connectdb.getConnection()
try:
    cursor=connection.cursor()
    sql = "INSERT INTO employee(emp_no,emp_name,emp_salary) VALUES (%s,%s,%s)"
    cursor.execute(sql,('61099','Shota','40000'))
    connection.commit()
    print("created employee")
except pymysql.Error as e:
    print("Error %s"% e.args[1])
finally:
    connection.close()