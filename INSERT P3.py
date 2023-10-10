
import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db")

# INSERT DATA INTO TABLE .

yy = xx.cursor()

sql = " insert into customers ( name , address ) values ( %s , %s ) "
val3 =  ( "ZAC" , "ITALY" ) 

yy.execute ( sql , val3 )
xx.commit()
print ( yy.lastrowid , "WAS LAST ROW" )
