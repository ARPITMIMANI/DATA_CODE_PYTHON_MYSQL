import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db" ) 

# CREATE A TABLE .

yy = xx.cursor()
# yy.execute ( "create table customers ( name varchar(255) , address varchar(255) ) " )

# ALTER A TABLE BY ADDING COLUMN .

yy.execute ( " alter table customers add column id int auto_increment primary key " )