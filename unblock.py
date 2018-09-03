import cx_Oracle
con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
cur=con.cursor()
acc_no=10004896
cur.execute("update block set status=1 where account_no=:ac",{'ac':acc_no})
con.commit()
con.close()
