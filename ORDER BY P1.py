# ORDER BY STATEMENT : SORT THE RESULT IN ASCENDING OR DESCENDING ORDER .

import mysql.connector
ww = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )

# SELECT DATA FROM THE TABLE USING ORDER BY STATEMENT .

xx = ww.cursor()
yy = " select * from customers order by name asc "
xx.execute(yy)

zz = xx.fetchall()
for i in zz:
    print(i)   