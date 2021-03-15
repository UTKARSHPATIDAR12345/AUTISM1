################################## IMPORT LIBRARIES ##################################

from flask import Flask, render_template, request, redirect, url_for
from flask import *
from form import userform, printdata, updateExcel, paidDetails, amountToPay, payToIndividual, indiMonthlyView, indiPayView, adjustform, updatekyc, deleteform, printdeldata, adjustpaymentform
#from flaskwebgui import FlaskUI
import tkinter as tk
from tkinter import messagebox as mb
from calculation import *
from pymsgbox import *
from flask import abort
from asd import *
import sqlite3
import os

################################## FLASK ##################################

app = Flask(__name__)
app.secret_key = 'gemscap'
#ui = FlaskUI(app)

imgFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = imgFolder

################################## ROUTE DEFAULT ##################################

@app.route('/')
def default():
	login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'bglogin1.jpg')
	return render_template('login_page.html', first_img = login_img)

database={'admin':'gemscap'}

################################## ROUTE LOGIN PAGE ##################################

@app.route('/login_page.html', methods = ['GET', 'POST'])
def login1():
	login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'bglogin1.jpg')
	return render_template('login_page.html', first_img = login_img)

################################## ROUTE FORM PAGE ##################################

@app.route('/form_login',methods=['GET' , 'POST'])
def login():
	login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'bglogin1.jpg')
	home_img = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
	email = request.form['email']
	password = request.form['password']
	if email not in database:
		return render_template('login_page.html' , info="Invalid Username", first_img = login_img)
	if database[email] != password:
		return render_template('login_page.html' , info="Invalid Password", first_img = login_img)
	else:
		return render_template('home.html', second_img = home_img)

################################## ROUTE HOME PAGE ##################################

@app.route('/home.html',methods=['GET' , 'POST'])
def home():
	return render_template('home.html')

################################## ROUTE USER PROFILE PAGE ##################################

@app.route('/user_profile.html',methods=['GET','POST'])
def userprofile():
	form = userform(request.form)
	print("form.errors is ", form.errors )
	if form.is_submitted():
		print("++++submitted+++")
	if not form.validate():
		print("++++invalid++++")
	print("form.errors2 is ", form.errors )
	
	if form.validate_on_submit():
		result = request.form
		print(result)
		## save in database here itself
		try:
			ID1 = request.form["ID1"]
			ID2 = request.form["ID2"]
			ID3 = request.form["ID3"]
			ID4 = request.form["ID4"]
			ID5 = request.form["ID5"]
			ID6 = request.form["ID6"]
			ID7 = request.form["ID7"]
			ID8 = request.form["ID8"]
			ID9 = request.form["ID9"]
			ID10 = request.form["ID10"]
			ID11 = request.form["ID11"]
			ID12 = request.form["ID12"]
			ID13 = request.form["ID13"]
			ID14 = request.form["ID14"]
			ID15 = request.form["ID15"]
			ID16 = request.form["ID16"]
			ID17 = request.form["ID17"]

			with sqlite3.connect("GEMSCAP_TABLE.db") as con:  
				cur = con.cursor() 
				#cur.execute('DROP TABLE gemscap_table')
				cur.execute('''CREATE TABLE IF NOT EXISTS gemscap_table(   
				EmployeeID TEXT NOT NULL,
				FirstName TEXT NOT NULL,
				MiddleName TEXT NOT NULL,
				LastName TEXT NOT NULL,
				FatherName TEXT NOT NULL,
				MotherName TEXT NOT NULL,
				DOB TEXT NOT NULL,
				Gender TEXT NOT NULL,
				MaritialStatus TEXT NOT NULL,
				PermanentAddress TEXT NOT NULL,
				City1 TEXT NOT NULL,
				Pincode1 INTEGER NOT NULL,
				Country1 TEXT NOT NULL,
				LocalAddress TEXT NOT NULL,
				City2 TEXT NOT NULL,
				Pincode2 INTEGER NOT NULL,
				Country2 TEXT NOT NULL,
				EmailAddress TEXT NOT NULL,
				ContactNumber1 INTEGER,
				ContactNumber2 INTEGER,
				FamilyPersonsName1 TEXT NOT NULL,
				FamilyPersonsContactNumber1 INTEGER,
				FamilyPersonsRelationWithEmployee1 TEXT NOT NULL,
				FamilyPersonsName2 TEXT NOT NULL,
				FamilyPersonsContactNumber2 TEXT NOT NULL,
				FamilyPersonsRelationWithEmployee2 TEXT NOT NULL,
				AadharCard TEXT NOT NULL,
				PanCard TEXT NOT NULL,
				EductionalCourseDetail TEXT NOT NULL,
				PassingYear INTEGER,
				PassingStatus TEXT NOT NULL,
				PFNomineeName TEXT NOT NULL,
				PFNomineeRelation TEXT NOT NULL,
				PFNomineeDOB TEXT NOT NULL,
				DateOfJoining TEXT NOT NULL,
				DateOfResigning TEXT NOT NULL,
				AccountNumber1 TEXT NOT NULL,
				IFSCcode1 TEXT NOT NULL,
				BankName1 TEXT NOT NULL,
				AccountType1 TEXT NOT NULL,
				AccountHolderName1 TEXT NOT NULL,
				AccountNumber2 TEXT NOT NULL,
				IFSCcode2 TEXT NOT NULL,
				BankName2 TEXT NOT NULL,
				AccountType2 TEXT NOT NULL,
				AccountHolderName2 TEXT NOT NULL,
				TakionID TEXT NOT NULL PRIMARY KEY,
				StartingBalance TEXT NOT NULL,
				PolicyNumber TEXT NOT NULL,
				CarryForwardBalance TEXT NOT NULL,
				RateOfDollar TEXT NOT NULL,
				Qty INT DEFAULT 0,
				Total FLOAT DEFAULT 0
				) 
				''') 
				cur.execute("INSERT INTO gemscap_table (EmployeeID,FirstName,MiddleName,LastName,FatherName,MotherName,DOB,Gender,MaritialStatus,PermanentAddress,City1,Pincode1,Country1,LocalAddress,City2,Pincode2,Country2,EmailAddress,ContactNumber1,ContactNumber2,FamilyPersonsName1,FamilyPersonsContactNumber1,FamilyPersonsRelationWithEmployee1,FamilyPersonsName2,FamilyPersonsContactNumber2,FamilyPersonsRelationWithEmployee2,AadharCard,PanCard,EductionalCourseDetail,PassingYear,PassingStatus,PFNomineeName,PFNomineeRelation,PFNomineeDOB,DateOfJoining,DateOfResigning,AccountNumber1,IFSCcode1,BankName1,AccountType1,AccountHolderName1,AccountNumber2,IFSCcode2,BankName2,AccountType2,AccountHolderName2,TakionID,StartingBalance,PolicyNumber,CarryForwardBalance,RateOfDollar) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (EmployeeID,FirstName,MiddleName,LastName,FatherName,MotherName,DOB,Gender,MaritialStatus,PermanentAddress,City1,Pincode1,Country1,LocalAddress,City2,Pincode2,Country2,EmailAddress,ContactNumber1,ContactNumber2,FamilyPersonsName1,FamilyPersonsContactNumber1,FamilyPersonsRelationWithEmployee1,FamilyPersonsName2,FamilyPersonsContactNumber2,FamilyPersonsRelationWithEmployee2,AadharCard,PanCard,EductionalCourseDetail,PassingYear,PassingStatus,PFNomineeName,PFNomineeRelation,PFNomineeDOB,DateOfJoining,DateOfResigning,AccountNumber1,IFSCcode1,BankName1,AccountType1,AccountHolderName1,AccountNumber2,IFSCcode2,BankName2,AccountType2,AccountHolderName2,TakionID,StartingBalance,PolicyNumber,CarryForwardBalance,RateOfDollar))
				con.commit()
				adduserto4tables(TakionID)                          ## 22 SEP
				msg = "Employee successfully Added"
				con.commit()  
				msg = "Employee successfully Added"  
		except:  
			con.rollback()  
			msg = "We can not add the employee to the list"  
		finally:
			return render_template('home.html', msg = msg)
			con.close()
		return redirect(url_for('saveDetails'))
		##render or code to save in dbms    
	return render_template('user_profile.html',form = form)

################################## ROUTE UPDATE PROFILE PAGE ##################################
	
@app.route('/update_kyc.html',methods=['GET','POST'])
def updateKYC():
	form = updatekyc(request.form)
	
	try:
		print("form.errors is ", form.errors )
		if form.is_submitted():
			print("++++submitted+++")
		if not form.validate():
			print("++++invalid++++")
		print("form.errors2 is ", form.errors )
		if request.method == 'POST' and form.validate_on_submit():		#request.method == 'POST' and form.is_submitted()
			result = request.form
			print(result)
			print(len(result))
			if(len(result) != 0):
				MaritialStatus = result["MaritialStatus"]
				LocalAddress = result["LocalAddress"]
				City2 = result["City2"]
				Pincode2 = result["Pincode2"]
				Country2 = result["Country2"]
				ContactNumber2 = result["ContactNumber2"]
				PFNomineeName = result["PFNomineeName"]
				PFNomineeRelation = result["PFNomineeRelation"]
				PFNomineeDOB = result["PFNomineeDOB"]
				DateOfResigning = result["DateOfResigning"]
				AccountNumber2 = result["AccountNumber2"]
				IFSCcode2 = result["IFSCcode2"]
				BankName2 = result["BankName2"]
				AccountType2 = result["AccountType2"]
				AccountHolderName2 = result["AccountHolderName2"]
				TakionID = result['TakionID']
				PolicyNumber = result['PolicyNumber']
				print("++++++++",MaritialStatus,City2,Pincode2,Country2)
				con = sqlite3.connect("GEMSCAP_TABLE.db")   
				cur = con.cursor()
				cur.execute('''UPDATE gemscap_table SET "MaritialStatus"="{}", ContactNumber2="{}", LocalAddress="{}", City2="{}",
							Pincode2="{}", Country2="{}", PFNomineeName="{}", PFNomineeRelation="{}", PFNomineeDOB="{}",  DateOfResigning="{}",
							AccountNumber2="{}",IFSCcode2="{}", BankName2="{}", AccountType2="{}", AccountHolderName2="{}", PolicyNumber="{}" 
							WHERE TakionID="{}"'''.format(MaritialStatus,ContactNumber2,LocalAddress,City2 ,Pincode2,Country2,PFNomineeName,PFNomineeRelation,PFNomineeDOB,DateOfResigning,AccountNumber2,IFSCcode2,BankName2,AccountType2,AccountHolderName2,PolicyNumber,TakionID)) 
				
				con.commit()
				con.close()
				return redirect(url_for('home'))
			if request.method == "GET":
				return render_template('update_kyc.html',form = form)
			
	except OSError as e:
		print(e)
	except ValueError as e:
		print(e)
	except NameError as e:
		print(e)
	except sqlite3.OperationalError as e:
		print(e)
	

	return render_template('update_kyc.html',form = form)

################################## ROUTE VIEW PAGE ##################################

@app.route("/view")  
def view():  
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	cur.execute("select * from gemscap_table")  
	rows = cur.fetchall()  
	return render_template("view.html",rows = rows)

################################## ROUTE VIEW DEL PAGE ##################################

@app.route("/viewdel")  
def viewdel():  
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	cur.execute("select * from deluser")  
	rows = cur.fetchall()  
	return render_template("viewdel.html",rows = rows)

################################## ROUTE EMPLOYEE DETAILS PAGE ##################################

@app.route("/Positive.html",methods = ["POST","GET"])
def tryprint():
    form=submit()
    if form.is_submitted():
		return redirect(url_for('Negativestimulus'))
	return render_template("Positive.html",form=form)

################################## ROUTE DELETED EMPLOYEE PAGE ##################################

@app.route("/tryprintdel.html",methods = ["POST","GET"])
def tryprintdel():
	form1 = printdata()
	return render_template("tryprintdel.html",form=form1)

################################## ROUTE VIEW INFORAMTION PAGE ##################################

@app.route("/trynew",methods = ["POST","GET"])
def trynew():
	#form1 = printdata()
	result = request.form
	z = result['EmployeeAccNo']
	print(z)
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	script="SELECT * FROM gemscap_table WHERE EmployeeID = '" + str(z) + "'"
	print(script)
	cur.execute(script)  
	rows = cur.fetchall()
	if len(rows) == 0:
		info="No such Employee ID Exists!"
		form = printdata()
		form.EmployeeAccNo.data = ""
		return render_template("tryprint.html",form=form,info=info)
	#print(rows)
	age = calculateage(z)
	return render_template("view.html",rows = rows, age = age)

################################## ROUTE DELETED INFORMATION PAGE ##################################

@app.route("/trynewdel",methods = ["POST","GET"])
def trynewdel():
	#form1 = printdata()
	result = request.form
	z = result['EmployeeAccNo']
	print(z)
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	script="SELECT * FROM deluser WHERE EmployeeID = '" + str(z) + "'"
	print(script)
	cur.execute(script)  
	rows = cur.fetchall()
	if len(rows) == 0:
		info="No such Employee ID Exists!"
		form = printdeldata()
		form.EmployeeAccNo.data = ""
		return render_template("tryprintdel.html",form=form,info=info)
	#print(rows)
	age = calculateage(z)
	return render_template("viewdel.html",rows = rows)

@app.route("/upload.html", methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		file = request.files["file"]
		file.save(os.path.join("uploads", file.filename))
	return render_template("/upload.html", message = "Successfully Uploaded")	

################################## ROUTE EXCELUPDATE PAGE ##################################

@app.route("/excelupdate.html",methods = ["POST","GET"])
def excelupdate():
	defaulterstr=''
	rows=[]
	form2 = updateExcel(request.form)
	if request.method == 'POST' and form2.is_submitted():
		m=form2.Month.data
		x=form2.Excel.data
		print(x,m)
		try:
			openfile(x)
			defaulterstr = createexceltable()

			defaultertkid = defaulterstr.split(' ')				###################### 28 SEP
			con = sqlite3.connect("GEMSCAP_TABLE.db")    
			cur = con.cursor()
			
			for i in range(len(defaultertkid)-1):
				cur.execute('SELECT TakionID,CarryForwardBalance,StartingBalance FROM gemscap_table WHERE TakionID = {}'.format(defaultertkid[i]))
				row = cur.fetchone()			#gives tuple
				rows.append(row)				#list of tuples
			con.commit()
			con.close()

			print("defaulters are ",defaulterstr)
			updatenetpay()
			updateCarryForwardBalance()
			updateCarryForwardBalanceInGemscap()
			updateMONTHLYTABLE(m)
			updateQuantitytable(m)
			updatetotaltable(m)
			updatetotalInGemscap()
			updatequantity()
			cleardata()

			form2.Excel.data=""
			return render_template("excelupdate.html",form=form2,defaulters = defaulterstr,rows=rows)
		except:
			pass
	form2.Excel.data=""		
	return render_template("excelupdate.html",form=form2,defaulters = defaulterstr,rows=rows)

################################## ROUTE PAID PAGE ##################################

@app.route("/paid.html", methods = ["POST", "GET"])  
def paid():  
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	#cur.execute("select * from gemscap_table")  
	cur.execute(''' SELECT gemscap_table.TakionID, round(CarryForwardBalance,2) as CarryForwardBalance, round(Jan,2) as Jan, round(Feb,2) as Feb,
					round(Mar,2) as Mar, round(Apr,2) as Apr, round(May,2) as May, round(Jun,2) as Jun, round(Jul,2) as Jul, round(Aug,2) as Aug, round(Sep,2) as Sep,
					round(Oct,2) as Oct, round(Nov,2) as Nov, round(Dec,2) as Dec FROM gemscap_table,MONTHLYTABLE WHERE gemscap_table.TakionID = MONTHLYTABLE.TAKIONID ''')

	rows = cur.fetchall()  
	con.commit()
	con.close()
	return render_template("paid.html",rows = rows)  

################################## ROUTE PAYMENT PAGE ##################################	

@app.route("/pay", methods=["GET","POST"])
def check():
	msg=''
	print("Hello")
	tkid = request.args.get('tkid')
	balance = request.args.get('bal')
	print(tkid)

	con = sqlite3.connect("GEMSCAP_TABLE.db")    
	cur = con.cursor()  
	cur.execute('''SELECT TAKIONID ,round(Jan,2) as Jan , round(Feb,2) as Feb , round(Mar,2) as Mar , round(Apr,2) as Apr , round(May,2) as May , round(Jun,2) 
					 as Jun , round(Jul,2) as Jul , round(Aug,2) as Aug , round(Sep,2) as Sep , round(Oct,2) as Oct , round(Nov,2) as Nov, round(Dec,2)
					 as Dec FROM MONTHLYTABLE WHERE MONTHLYTABLE.TAKIONID={}'''.format(tkid))
	row = cur.fetchone()
	con.commit()
	con.close()

	print(tkid,balance)
	form6 = payToIndividual()
	if request.method == 'POST' and form6.is_submitted():
		try:
			print("form submitted")
			m=request.form['Month']
			x=request.form['PayAmount']
			print(m,x)
			#check if amount is greater than month                                   ####17 sep
			check = checkamount(m,x,tkid)
			print("check is:",check)
			if check == True:
				print("inside if")
				updatePAIDTABLE(m,x,tkid)
				return redirect(url_for('paid'))
			else:
				print("inside else")
				
				root= tk.Tk()
				canvas1 = tk.Canvas(root, width = 3, height = 3)
				canvas1.pack()
				
				
				if mb.askyesno('Verify', 'Do you want to pay more than Earned?'):
					print("selected yes")
					updatePAIDTABLE(m,x,tkid)
				else:
					print("selected no")
				root.destroy()
				tk.mainloop()
				form6.PayAmount.data = ""
				#print("checkvalue = ",value)
				'''
				value = confirm(text='Do you want to pay more than Earned?', title='Attention!!', buttons=['YES', 'NO'])
				print(value)
				if value == 'YES':
					updatePAIDTABLE(m,x,tkid)
					return redirect(url_for('paid'))
				elif value == 'NO':
					return redirect(url_for('paid'))
				'''
		
		except:
			pass
	##create form accept month and amount to pay then call updatepaidtable() and also update cfb in gemscap_table
	return render_template('/indiPay.html', form = form6,msg=msg,row=row)
	#return render_template('/paid.html')

#@app.route("/indiMonthly",methods = ["POST","GET"])
#def trynew1():
#	#form1 = printdata()
#	result = request.form
#	z = result['TakionId']
#	print(z)
#	con = sqlite3.connect("GEMSCAP_TABLE.db")  
#	con.row_factory = sqlite3.Row  
#	cur = con.cursor()  
#	script="SELECT * FROM MONTHLYTABLE WHERE TAKIONID = '" + str(z) + "'"
#	print(script)
#	cur.execute(script)  
#	rows = cur.fetchall()
#	#print(rows)
#	return render_template("monthlyview.html",rows = rows)

################################## ROUTE PAYVIEW PAGE ##################################

@app.route("/payview", methods = ["POST","GET"])
def trynew2():
	#form1 = printdata()
	result = request.form
	z = result['TakionId']
	print(z)
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	script="SELECT * FROM PAIDTABLE WHERE TAKIONID = '" + str(z) + "'"
	print(script)
	cur.execute(script)  
	rows = cur.fetchall()
	#print(rows)
	return render_template("indipay.html", rows = rows)

################################## ROUTE PAIDVIEW PAGE ##################################

@app.route("/paidview.html",methods = ["POST","GET"])
def tryprint2():
	form8 = indiPayView()
	return render_template("paidview.html",form=form8)

################################## ROUTE ADJUST PAGE ##################################

@app.route("/adjust.html",methods=["GET" , "POST"])
def adjust():
	form=adjustform()
	info=""
	if form.is_submitted() and request.method == "POST":
		try:
			tk = request.form['Takionid']
			month = request.form['Month']
			amount = request.form['Amount']
			print(tk,month,amount)
			##function call to update cfb in gemscaptable and monthly tale
			adjustcfbingemscap_adjustmonthlytable(tk,amount,month)
			
			return render_template('/adjust.html',info=info , form=form)
		except:
			pass
	return render_template('/adjust.html', form=form)

################################## ROUTE QUANTITY PAGE ##################################

@app.route("/quantity.html",methods=["GET","POST"])
def quantity():
	con = sqlite3.connect("GEMSCAP_TABLE.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	cur.execute(''' SELECT  TAKIONID ,round(Jan,2) as Jan , round(Feb,2) as Feb , round(Mar,2) as Mar , round(Apr,2) as Apr , round(May,2) as May , round(Jun,2) 
					 as Jun , round(Jul,2) as Jul , round(Aug,2) as Aug , round(Sep,2) as Sep , round(Oct,2) as Oct , round(Nov,2) as Nov, round(Dec,2)
					 as Dec FROM QUANTITYTABLE''')  
	#cur.execute(''' SELECT gemscap_table.TakionID,CarryForwardBalance,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec FROM gemscap_table,MONTHLYTABLE  ''')
	rows = cur.fetchall()  
	return render_template("quantity.html",rows = rows)

################################## ROUTE SUMMARY PAGE ##################################

@app.route("/summary.html",methods=["GET","POST"])
def printIndiSummary():
	tkid = request.args.get('tkid')
	conn = sqlite3.connect("GEMSCAP_TABLE.db") 
	conn.row_factory = sqlite3.Row    
	curs = conn.cursor()
	curs.execute(''' SELECT  TAKIONID ,round(Jan,2) as Jan , round(Feb,2) as Feb , round(Mar,2) as Mar , round(Apr,2) as Apr , round(May,2) as May , round(Jun,2) 
					 as Jun , round(Jul,2) as Jul , round(Aug,2) as Aug , round(Sep,2) as Sep , round(Oct,2) as Oct , round(Nov,2) as Nov, round(Dec,2)
					 as Dec FROM TOTALTABLE WHERE TAKIONID = {} 
					 UNION ALL
					 SELECT TAKIONID ,round(Jan,2) as Jan , round(Feb,2) as Feb , round(Mar,2) as Mar , round(Apr,2) as Apr , round(May,2) as May , round(Jun,2) 
					 as Jun , round(Jul,2) as Jul , round(Aug,2) as Aug , round(Sep,2) as Sep , round(Oct,2) as Oct , round(Nov,2) as Nov, round(Dec,2)
					 as Dec FROM MONTHLYTABLE WHERE TAKIONID = {} 
					 UNION ALL
					 SELECT TAKIONID ,round(Jan,2) as Jan , round(Feb,2) as Feb , round(Mar,2) as Mar , round(Apr,2) as Apr , round(May,2) as May , round(Jun,2) 
					 as Jun , round(Jul,2) as Jul , round(Aug,2) as Aug , round(Sep,2) as Sep , round(Oct,2) as Oct , round(Nov,2) as Nov, round(Dec,2)
					 as Dec FROM PAIDTABLE WHERE TAKIONID = {}
				'''.format(tkid,tkid,tkid))
	rows = curs.fetchall()           
	#Name tkid starting_balance cfb  policy joining_date
	curs.execute(''' SELECT FirstName,round(StartingBalance,2) as StartingBalance,round(CarryForwardBalance,2) as CarryForwardBalance,PolicyNumber,DateOfJoining FROM
					 gemscap_table WHERE TakionID = {}'''.format(tkid))
	info = curs.fetchone()
	
	conn.commit()                                               ##conn not closed in /paid in route 
	conn.close()
	return render_template("summary.html",row1 = rows[0] , row2 = rows[1] , row3 = rows[2],info=info,tkid=tkid)

################################## ROUTE DELETE PAGE ##################################

@app.route('/delete.html' , methods = ["GET" , "POST"])
def delete():
	form=deleteform()
	info = "" 	
	if form.is_submitted() and request.method == "POST":
		try:
			tkid = request.form['TakionID']
			print(tkid)
			ans = deluser(tkid)
			if ans == False:
				info = "No such Takion ID Exists!"
			form.TakionID.data=""
			return render_template('/delete.html', form=form, info = info)
		except:
			pass
	form.TakionID.data=""
	return render_template('/delete.html', form=form)

################################## ROUTE PAYMENT ADJUST PAGE ##################################

@app.route("/tryprintadjustpay.html",methods=["GET" , "POST"])   ########1/11/2020 Adjust Payment (tryprintadjustpay.html)########
def adjustpay():
	form=adjustpaymentform()
	info=""
	if form.is_submitted() and request.method == "POST":
		try:
			tk = request.form['Takionid']
			month = request.form['Month']
			amount = request.form['Amount']
			print(tk,month,amount)
			##function call to update cfb in gemscaptable and monthly tale
			adjustpaymentinpaymenttable(tk,amount,month)
			
			return render_template('/tryprintadjustpay.html',info=info , form=form)
		except:
			pass
	return render_template('/tryprintadjustpay.html', form=form)



@app.route('/negative.html',methods=['GET','POST'])
def Negativestimulus():
	return render_template('/negative.html')
################################## MAIN ##################################

if __name__ == "__main__":
	app.run(debug = True)
	#ui.run()	