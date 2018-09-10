import cx_Oracle
con = cx_Oracle.connect('SYSTEM/user123@localhost/xe')
cur = con.cursor()
counter=10004896
try:
    cur.execute(""" CREATE TABLE Bank_Details(Account_No Number(10) PRIMARY KEY ,Adhar_no Number(12) UNIQUE check(length(adhar_no)=12),Name Varchar2(30) NOT NULL,Date_of_Birth Varchar2(20) NOT NULL,Mobile_no Number(10) NOT NULL check(length(mobile_no)=10),Opening_Date Varchar2(20),PIN NUMBER(4) NOT NULL UNIQUE check(length(PIN)=4),Balance NUMBER(20))""")
    cur.executemany(""" INSERT INTO Bank_Details VALUES(:1,:2,:3,:4,:5,:6,:7,:8)""",[(counter,111111111111,'Anmol','13-sep-2000',1593574789,'10-dec-2015',1596,'12000'),(counter+1,222222222222,'Ishaan','13-jan-2000',3654862486,'12-jun-2017',7001,'50000'),(counter+2,333333333333,'Keshav','12-jun-1999',1478963478,'20-may-2016',1056,'20000'),(counter+3,564845691236,'Ankush','06-feb-2000',1236987478,'24-jan-2017',8040,'35000')])
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("error",e)
finally:
    con.close()
    
