import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )  

# UPDATE RECORDS FROM THE TABLE .

yy = xx.cursor()
zz = " update customers set address='SPAIN' where address='POLAND' "
yy.execute(zz)

# ww.commit() IS USED TO DELETE PERMANENTLY FROM THE TABLE .

print ( yy.rowcount , " RECORDS UPDATED " ) 
