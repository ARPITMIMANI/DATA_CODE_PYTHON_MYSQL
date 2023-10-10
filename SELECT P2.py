import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db")

# SELECT DATA FROM THE TABLE .

yy = xx.cursor()
yy.execute ( " select name , address from customers " )

zz = yy.fetchall()
for i in zz:
    print(i)