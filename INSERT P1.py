import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db")

# INSERT DATA INTO TABLE .

yy = xx.cursor()

sql = " insert into customers ( name , address ) values ( %s , %s ) "
val1 = ( "TOM" , "GERMANY" )

yy.execute ( sql , val1 )
xx.commit()
print ( yy.rowcount , "RECORD INSERTED" )

# commit() IS VERY IMPORTANT FOR SAVING THE CHANGES PERMANENTLY .