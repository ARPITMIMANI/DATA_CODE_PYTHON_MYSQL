import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" ) 

# CHECK IF THE TABLE EXISTS OR NOT .

yy = xx.cursor()
yy.execute ( "show tables" )

for i in yy:
    print(i)
