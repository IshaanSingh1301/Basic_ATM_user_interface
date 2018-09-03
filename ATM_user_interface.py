import datetime
import random
def debit(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	tran=(random.randrange(100000,10000000,3))
	cur.execute("select status from block where account_no=:accc",{'accc':account_no})
	for row in cur:
		row=int(row[0])
	if(row<4):
		pin=int(input("Enter PIN"))
		cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
		for line in cur:
			k=int(line[0])
		if(k==pin):
			cur.execute("update block set status=1 where account_no=:aco",{'aco':account_no})
			cur.execute("select name from bank_details where PIN=:pine and account_no=:yup",{'pine':pin,'yup':account_no})
			for row in cur:
				print(row)
			debit_amount = int(input("Enter the debit amount"))
	
	
	
			cur.execute("select balance from Bank_Details where pin=:p and Account_no=:acn",{'p':pin,'acn':account_no})
			for line in cur:
				balance=line[0]
			if (debit_amount<balance):
				updated_balance = balance-debit_amount
		
#code starts
				cur.execute("UPDATE Bank_Details SET Balance = :balanc where PIN = :pn",{'balanc':updated_balance,'pn':pin})#Update the balance in the Accounts table
				cur.execute("INSERT into Debits values(:account_no ,:dat ,:debit_amount,:tran_id)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount,'tran_id':tran})#Insert Query#
#code ends
				con.commit()
				print("Wait we are processing your request......")
				time.sleep(10)
				print("Transaction successful")
				time.sleep(3)
				cur.execute("select Balance from bank_details where Account_no=:ac and pin=:j",{'ac':account_no,'j':pin})
				for row in cur:
					print("Available balance:",row)
				cur.execute("select transaction_date from debits join bank_details on debits.account_no=bank_details.account_no where debits.Transaction_id=:tr and bank_details.pin=:ty",{'tr':tran,'ty':pin})
				for row in cur:
					print("Transaction done on:",row)
				cur.close()
				con.close()
			else:
				print("insufficient Balance")
		else:
			print("Incorrect PIN")
			block(account_no)
			recall1(account_no)
	else:
		print("account blocked")



import datetime
import random
def block(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	tran=(random.randrange(100000,10000000,3))
	cur.execute("select status from block where account_no=:accc",{'accc':account_no})
	for row in cur:
		row=int(row[0])
	sit=row+1
	cur.execute("update block set status=:st where account_no=:ac",{'st':sit,'ac':account_no})
	con.commit()
	con.close()



def recall1(account_no):
	debit(account_no)
	

import cx_Oracle
import time
import datetime
import random
def changepin(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	debit_amount=0
	tran=(random.randrange(1546846,3216548321,3))
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
#please fetch the current balance from the accounts table and store it in the variable named balance
	print("Change your PIN")
	pin = int(input("Enter the previous PIN or Adhar number"))
	cur.execute("select name from bank_details where (PIN=:pine or adhar_no=:adn) and account_no=:yup",{'pine':pin,'adn':pin,'yup':account_no})
	for row in cur:
		print(row)
	cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
	for line in cur:
		k=int(line[0])
	if(k==pin):			
		new=int(input("Enter new PIN"))
	
	
	
#code starts
		cur.execute("UPDATE Bank_Details SET PIN = :p where (PIN = :pn or Adhar_no=:ad) and Account_no=:ac",{'pn':pin,'ad':pin,'ac':account_no,'p':new})#Update the balance in the Accounts table
#Insert Query#
		cur.execute("INSERT into Debits values(:account_no ,:dat ,:debit_amount,:tran_id)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount,'tran_id':tran})
	
	
		con.commit()
		cur.execute("select transaction_date from debits join bank_details on debits.account_no=bank_details.account_no where debits.transaction_id=:tr and bank_details.account_no=:pn",{'tr':tran,'pn':account_no})
		for row in cur:
			x=row
		cur.close()
		con.close()
		print("Wait we are processing your request......")
		time.sleep(2)
		print("PIN changed\nTransaction date",x,"\nTransaction successful")
	else:
		print("incorrect PIN")

	
import cx_Oracle
import time
import datetime
import random
def adhar(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	debit_amount=0
	tran=(random.randrange(1546846,3216548321,3))
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	pin=int(input("Enter PIN"))
	cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
	for line in cur:
		k=int(line[0])
	if(k==pin):
		cur.execute("select name from bank_details where PIN=:pine and account_no=:yup",{'pine':pin,'yup':account_no})
		for row in cur:
			print(row)
		new=int(input("Enter new Adhar Number"))
	
	
#code starts
		cur.execute("UPDATE Bank_Details SET Adhar_no = :adh where PIN = :pin and Account_no=:an",{'pin':pin,'an':account_no,'adh':new})#Update the balance in the Accounts table
		cur.execute("INSERT into Debits values(:account_no ,:dat ,:debit_amount,:tran_id)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount,'tran_id':tran})
#code ends
		con.commit()
		cur.execute("select transaction_date from debits join bank_details on debits.account_no=bank_details.account_no where debits.transaction_id=:tr and bank_details.pin=:pn",{'tr':tran,'pn':pin})
		for row in cur:
			x=row
		cur.close()
		con.close()
		print("Wait we are processing your request......")
		time.sleep(10)
		print("Adhaar Number updated\nTransaction date",x,"\nTransaction successful")
	else:
		print("Incorrect PIN")



import cx_Oracle
import time
import datetime
import random
def dob(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	debit_amount=0
	tran=(random.randrange(1546846,3216548321,3))
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	pin=int(input("Enter PIN"))
	cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
	for line in cur:
		k=int(line[0])
	if(k==pin):
		cur.execute("select name from bank_details where PIN=:pine and account_no=:yup",{'pine':pin,'yup':account_no})
		for row in cur:
			print(row)
		new=str(input("Enter new Date of Birth like: 11-sept-2000"))
	
	
#code starts
		cur.execute("UPDATE Bank_Details SET Date_of_Birth = :dob where PIN = :pin and Account_no=:an",{'pin':pin,'an':account_no,'dob':new})#Update the balance in the Accounts table
		cur.execute("INSERT into Debits values(:account_no ,:dat ,:debit_amount,:tran_id)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount,'tran_id':tran})
#code ends
		con.commit()
		cur.execute("select transaction_date from debits join bank_details on debits.account_no=bank_details.account_no where debits.transaction_id=:tr and bank_details.pin=:pn",{'tr':tran,'pn':pin})
		for row in cur:
			x=row
		cur.close()
		con.close()
		print("Wait we are processing your request......")
		time.sleep(10)
		print("Date of Birth updated\nTransaction date",x,"\nTransaction successful")
	else:
		print("Incorrect PIN")



def options(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	print("**(1)UPDATE ADHAR NUMBER**                              **(2)UPDATE DATE OF BIRTH**\n**(3)UPDATE MOBILE NUMBER**                             **(4)BALANCE ENQUIRY**")
	i=int(input("Enter Service you want"))
#code starts
	if(i==1):
		adhar(account_no)
	if(i==2):
		dob(account_no)
	if(i==3):
		mob(account_no)
	if(i==4):
		bal(account_no)
	
#code ends
	
	cur.close()
	con.close()
	

import cx_Oracle
import time
import datetime
import random
def mob(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	debit_amount=0
	tran=(random.randrange(1546846,3216548321,3))
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	pin=int(input("Enter PIN"))
	cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
	for line in cur:
		k=int(line[0])
	if(k==pin):
		cur.execute("select name from bank_details where PIN=:pine and account_no=:yup",{'pine':pin,'yup':account_no})
		for row in cur:
			print(row)
		new=int(input("Enter new mobile no"))
	
	
#code starts
		cur.execute("UPDATE Bank_Details SET Mobile_no = :mb where PIN = :pin and Account_no=:an",{'pin':pin,'an':account_no,'mb':new})#Update the balance in the Accounts table
		cur.execute("INSERT into Debits values(:account_no ,:dat ,:debit_amount,:tran_id)",{'account_no':account_no,'dat':a,'debit_amount':debit_amount,'tran_id':tran})
#code ends
		con.commit()
		cur.execute("select transaction_date from debits join bank_details on debits.account_no=bank_details.account_no where debits.transaction_id=:tr and bank_details.pin=gn",{'tr':tran,'gn':pin})
		for row in cur:
			x=row
	
	
		print("Wait we are processing your request......")
		time.sleep(10)
		print("Mobile number updated\nTransaction date",x,"\nTransaction successful")
		cur.close()
		con.close()
	else:
		print("Incorrect PIN")

import cx_Oracle
import time
import datetime
def bal(account_no):
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	
	now = datetime.datetime.now()
	a=(now.strftime("%Y-%m-%d"))
	
	pin=int(input("Enter PIN"))
	cur.execute("select PIN from bank_details where account_no=:acn",{'acn':account_no})
	for line in cur:
		k=int(line[0])
	if(k==pin):
		cur.execute("select name from bank_details where PIN=:pine and account_no=:yup",{'pine':pin,'yup':account_no})
		for row in cur:
			row=str(row[0])
			l=row.upper()
			print(l)
	
#code starts
		cur.execute("select Balance from Bank_Details where PIN = :pin and Account_no=:an",{'pin':pin,'an':account_no})#Update the balance in the Accounts table
		for row in cur:
			print("Please wait......we are proccessing you request........")
			time.sleep(10)
			print("Your current balance in account is :",row)
#code ends
	
		con.commit()
		cur.close()
		con.close()
	
		time.sleep(2)
		print("\nTransaction Complete")
		time.sleep(2)
		print("\nThank You")
	else:
		print("Incorrect PIN")



def identification():
	con=cx_Oracle.connect("SYSTEM/user123@localhost/xe")
	cur=con.cursor()
	print("Hello Sir, Welcome to ABC bank. Here you can debit credit the amount and also you could see the list of last transaction you made.")
	print("So please enter pin to proceed.")
	account_no=int(input("Enter account number "))
	
	try:
		cur.execute("select * from Bank_Details where Account_no =:Acc",{'Acc':account_no})
		for line in cur:
			account_no=line[0]
		cur.execute("select count(*) from Bank_Details where account_no=:acn",{'acn':account_no})
		for row in cur:
			row=int(row[0])
		if(row==1):
			print("So please select the following:\n**(1)PIN CHANGE**\n**(2)WITHDRAWL**                                        **(3)BANK ACCOUNT SERVICES**")
			i=int(input("Enter your choice: "))
			if (i==1):
				changepin(account_no)
			if (i==2):
				debit(account_no)
			if(i==3):
				options(account_no)
			if (i>3):
				print("Wrong choice....")
		else:
			print("This account number does not exist")
	except cx_Oracle.DatabaseError as e:
		print(e)
		print("Logon denied....Please Check your pin.")
	
identification()
