import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" )

# THE MYSQL cursor() OF mysql-connector-python  IS USED TO EXECUTE STATEMENTS TO COMMUNICATE WITH THE MYSQL DATABASE .

# CREATE A DATABASE .

yy = xx.cursor()
yy.execute ( "create database data_code_db" )
   