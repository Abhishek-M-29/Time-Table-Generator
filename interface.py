import mysql.connector as sql

con = sql.connect(host='localhost', user='root', passwd='admin', database='nothing')

if con.is_connected():
    print('Done')

