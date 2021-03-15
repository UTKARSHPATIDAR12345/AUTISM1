import sqlite3

def createMONTHLYTABLE():
    print("createMONTHLYTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    #cur.execute('DROP TABLE MONTHLYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS MONTHLYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO MONTHLYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key canstraint")
    
    #cur.execute('UPDATE MONTHLYTABLE SET (Jan,Feb) = ({},{}) where TAKIONID=12324'.format(100,200))

    con.commit()
    con.close()

#######################################################################################################

def createPaidtable():
    print("createPaidtable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE PAIDTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS PAIDTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO PAIDTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################

def createQuantitytable():
    print("createQuantitytable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE QUANTITYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS QUANTITYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO QUANTITYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################

def createtotaltable():
    print("createtotaltable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE TOTALTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS TOTALTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO TOTALTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################

def updatetotaltable(month):
    print("inside updatetotaltable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute('''UPDATE TOTALTABLE 
                    SET
      {} = {} + (SELECT EXCELTABLE.TOTAL_DELTA 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = TOTALTABLE.TAKIONID )
    WHERE
        EXISTS (
            SELECT *
            FROM EXCELTABLE
            WHERE EXCELTABLE.TAKIONID = TOTALTABLE.TAKIONID)'''.format(month,month))
    con.commit()
    con.close()

#######################################################################################################

def updateQuantitytable(month):
    print("inside updateQuantitytable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute(''' UPDATE QUANTITYTABLE
                    SET
                    {} = {} + (SELECT EXCELTABLE.QUANTITY 
                               FROM EXCELTABLE
                               WHERE EXCELTABLE.TAKIONID = QUANTITYTABLE.TAKIONID)
                    WHERE
                    EXISTS (
                    SELECT *
                    FROM EXCELTABLE
                    WHERE EXCELTABLE.TAKIONID = QUANTITYTABLE.TAKIONID)'''.format(month,month))
    cur.execute(''' UPDATE gemscap_table
                    SET
                    Qty = Qty + (SELECT EXCELTABLE.QUANTITY 
                               FROM EXCELTABLE
                               WHERE EXCELTABLE.TAKIONID = gemscap_table.TAKIONID)
                    WHERE
                    EXISTS (
                    SELECT *
                    FROM EXCELTABLE
                    WHERE EXCELTABLE.TAKIONID = gemscap_table.TAKIONID)''')
    con.commit()
    con.close()

#######################################################################################################

def updateMONTHLYTABLE(month):
    month = str(month)
    print("inside updateMONTHLYTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('''UPDATE MONTHLYTABLE 
                    SET
      {} = {} + (SELECT EXCELTABLE.NetPay 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = MONTHLYTABLE.TAKIONID )
    WHERE
        EXISTS (
            SELECT *
            FROM EXCELTABLE
            WHERE EXCELTABLE.TAKIONID = MONTHLYTABLE.TAKIONID)'''.format(month,month))

    con.commit()
    con.close()

#######################################################################################################

def updatePAIDTABLE(month,payment,tk):
    month = str(month)
    payment=float(payment)
    tk=int(tk)
    print("inside updatePAIDTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('UPDATE PAIDTABLE SET {} = {} where TAKIONID = {}'.format(month,payment,tk) )
    cur.execute('UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance - {} WHERE TakionID = {}'.format(payment,tk) )

    con.commit()
    con.close()

#######################################################################################################

def checkamount(month,amount,tkid):
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('SELECT {} FROM MONTHLYTABLE WHERE TAKIONID = {}'.format(month,tkid))
    month_amt = cur.fetchone()

    con.commit()
    con.close()
    print("amount is",amount," month_amt is",month_amt[0])
    if(float(amount) <= float(month_amt[0])):
        return True
    return False

#######################################################################################################

def adduserto4tables(tkid):     
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute('INSERT INTO PAIDTABLE (TAKIONID) VALUES ({})'.format(tkid)) 
    cur.execute('INSERT INTO TOTALTABLE (TAKIONID) VALUES ({})'.format(tkid))    
    cur.execute('INSERT INTO MONTHLYTABLE (TAKIONID) VALUES ({})'.format(tkid)) 
    cur.execute('INSERT INTO QUANTITYTABLE (TAKIONID) VALUES ({})'.format(tkid)) 
    con.commit()
    con.close()
####################################    27 sept
def createdeluser():
    print("createdeluser creating")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    #cur.execute('DROP TABLE deluser')
    cur.execute('''CREATE TABLE IF NOT EXISTS deluser(   
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
				TakionID TEXT NOT NULL,
				StartingBalance TEXT NOT NULL,
				PolicyNumber TEXT NOT NULL,
				CarryForwardBalance TEXT NOT NULL,
				RateOfDollar TEXT NOT NULL,
				Qty INT DEFAULT 0,
				Total FLOAT DEFAULT 0) ''')
    con.commit()
    con.close()

def deluser(tkid):
    print("inside deluser takionid is: ",tkid)
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('SELECT * FROM gemscap_table WHERE TakionID = {}'.format(tkid))
    row = cur.fetchone()
    if row == None:
        return False
    print(row)

    cur.execute('INSERT INTO deluser SELECT * FROM gemscap_table WHERE TakionID={}'.format(tkid))
    cur.execute('DELETE FROM gemscap_table WHERE TakionID={}'.format(tkid))
    cur.execute('DELETE FROM MONTHLYTABLE WHERE TAKIONID={}'.format(tkid))
    cur.execute('DELETE FROM PAIDTABLE WHERE TAKIONID={}'.format(tkid))
    cur.execute('DELETE FROM QUANTITYTABLE WHERE TAKIONID={}'.format(tkid))
    cur.execute('DELETE FROM TOTALTABLE WHERE TAKIONID={}'.format(tkid))
    con.commit()
    con.close()
    return True

##########    15 september for adjusting cfb of a takionid
def adjustcfbingemscap_adjustmonthlytable(tk,amount,month):
    print('INSIDE adjustcfbingemscap_adjustmonthlytable')
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance + {} WHERE Takionid = {}'.format(amount,tk))
    cur.execute('UPDATE MONTHLYTABLE SET {} = {} + {} WHERE TAKIONID = {}'.format(month,month,amount,tk))

    con.commit()
    con.close()

##########    1 November for adjusting payment of a takionid
def adjustpaymentinpaymenttable(tk,amount,month):
    print('INSIDE adjustpaymentform')
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute('UPDATE PAIDTABLE SET {} = {} + {} WHERE TAKIONID = {}'.format(month,month,amount,tk))

    con.commit()
    con.close()

# createMONTHLYTABLE()   figure out how to call this all create func once
# createPaidtable()
# createQuantitytable()

# updateMONTHLYTABLE('Feb')
# updatePAIDTABLE('Feb',200,12324)

# createtotaltable()

#createdeluser()