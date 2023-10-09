import mysql.connector
ww = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )

# SELECT DATA FROM THE TABLE USING ORDER BY STATEMENT .

xx = ww.cursor()
yy = " select * from customers limit 4 offset 6 "
xx.execute(yy)

zz = xx.fetchall()
for i in zz:
    print(i)

# HERE WE STARTED FROM ROW POSITION 7 AND RETURN 4 RECORDS .    