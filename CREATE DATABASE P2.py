import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" ) 
print(xx)

# CHECK IF THE DATABASE EXISTS OR NOT .

yy = xx.cursor()
yy.execute ( "show databases" )

# CODE 01

zz = yy.fetchall()
for i in zz:
    print(i)

# CODE 02 

for j in yy:
     print(j)      
