import cx_Oracle
con = cx_Oracle.connect('system/user123@localhost/xe')
cur = con.cursor()
try:
    
    cur.execute(""" CREATE TABLE  Debits(Account_No Number(10),Transaction_Date varchar2(20),Debit_Amount Number(20),Transaction_id Number(20) UNIQUE NOT NULL,FOREIGN KEY(Account_No) REFERENCES Bank_Details(Account_No))""")
    
    con.commit()
except cx_Oracle.DatabaseError as e:
    print("error",e)
finally:
    con.close()
