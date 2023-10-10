import mysql.connector
xx = mysql.connector.connect ( host="localhost" , user="root" , password="SQLSERVER2019" , port="3306" , database="data_code_db")

# INSERT DATA INTO TABLE .

yy = xx.cursor()

sql = " insert into customers ( name , address ) values ( %s , %s ) "

val2 = [ ( "LEO" , "ITALY" ) , 
         ( "GUY" , "POLAND" ) , 
         ( "RIO" , "DENMARK" ) ,    
         ( "SAM" , "FRANCE" ) , 
         ( "JIM" , "ITALY" ) , 
         ( "KOA" , "POLAND" ) , 
         ( "ASH" , "GERMANY" ) , 
         ( "MAC" , "DENMARK" ) , 
         ( "OLI" , "POLAND" ) ,    
         ( "NEO" , "GERMANY" ) ,
         ( "FOX" , "FRANCE" ) , 
         ( "DAX" , "POLAND" ) ,  
         ( "BOB" , "ITALY" ) , 
         ( "PEN" , "DENMARK" ) ]

yy.executemany ( sql , val2 )
xx.commit()
print ( yy.rowcount , "ROWS INSERTED" )
