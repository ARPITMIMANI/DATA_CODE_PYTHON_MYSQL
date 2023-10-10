# DROP TABLE STATEMENT : DELELTE THE EXISTING TABLE FROM THE DATABASE .

import mysql.connector
ww = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" )

# DELETE THE ENTIRE TABLE .

xx = ww.cursor()
yy = " drop table cus_table "
xx.execute(yy)

# ww.commit() IS USED TO DELETE PERMANENTLY FROM THE TABLE .
