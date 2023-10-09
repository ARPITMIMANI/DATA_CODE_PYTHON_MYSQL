import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db")

# SELECT DATA FROM THE TABLE .

yy = xx.cursor()
yy.execute ( " select * from customers " )
zz = yy.fetchone()
print(zz)

# fetchone() IS USED TO RETURN ONLY THE FIRST ROW OF THE RESULT .
