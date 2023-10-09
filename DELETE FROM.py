import mysql.connector
ww = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )

# DELETE DATA FROM THE TABLE .

xx = ww.cursor()
yy = "delete from customers where address='france' "
xx.execute(yy)

# ww.commit() IS USED TO DELETE PERMANENTLY FROM THE TABLE .

print ( xx.rowcount , " RECORDS DELETED " )
