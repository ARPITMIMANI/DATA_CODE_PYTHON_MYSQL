# PYTHON NEEDS A SQL DRIVER TO ACCESS THE MYSQL DATABASE .

# CODE 01

import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" )
print(xx)

# CODE 02

import mysql.connector as myc
yy = myc.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" )
print(yy)

# CODE 03

import mysql.connector as myc
zz = myc.connect ( host="localhost" , user="root" , password="SQLSERVER2019" )
print(zz)