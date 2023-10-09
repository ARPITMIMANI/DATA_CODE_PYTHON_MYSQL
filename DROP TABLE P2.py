import mysql.connector
ww = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )

# DELETE THE ENTIRE TABLE .

xx = ww.cursor()
yy = " drop table if exists cus_table "
xx.execute(yy)

# ww.commit() IS USED TO DELETE PERMANENTLY FROM THE TABLE .

# "IF EXISTS" IS USED TO DROP OR DELETE TABLE IF IT EXISTS AND EXECUTES WITHOUT ANY ERROR . 



