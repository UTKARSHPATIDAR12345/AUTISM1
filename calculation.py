import xlrd
import sqlite3
from datetime import date

TKID = []
total_d=[]
payable=[]
qty=[]

#######################################################################################################

def openfile(x):
    print("INSIDE openfile()")
    loc=(r'/home/aadarsh/Desktop/GEMSCAP_boot/'+x+'.xls') #loc=(r'.....\downloads\ + file name + .xls')
    print(loc)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0) 
    global TKID 
    global total_d
    global qty
    TKID=sheet.col_values(0,1,sheet.nrows-4)
    total_d=sheet.col_values(31, 1, sheet.nrows-4)
    qty=sheet.col_values(4, 1, sheet.nrows-4)
    qty = [i/1000 for i in qty] 

    for i in range (len(TKID)):
        TKID[i]=TKID[i].replace(" ","")
    #TKID=list(dict.fromkeys(TKID))

    #total_d = [i for i in total_d if i != '']

    print("LENGTH OF TKID: ",len(TKID))
    print(TKID)
    print("LENGTH OF total_d: ",len(total_d))
    print(total_d)
    print("LENGTH OF qty: ",len(qty))
    print(qty)

#######################################################################################################

def createexceltable():
    print("INSIDE createexceltable()")
    defaulterstr = ''
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    print("checkpoint 1****")
    cur.execute('DROP TABLE EXCELTABLE')
    cur.execute("""CREATE TABLE EXCELTABLE (TAKIONID INT  ,
                TOTAL_DELTA FLOAT DEFAULT 0 , PolicyNumber INT DEFAULT 0, NetPay FLOAT DEFAULT 0 , PAID FLOAT , TOTAL FLOAT  ,
                CarryForwardBalance FLOAT DEFAULT 0, StartingBalance FLOAT DEFAULT 0, QUANTITY INT)""")
    print("checkpoint 2****")
    for i in range(len(TKID)):
        
        cur.execute('''INSERT INTO EXCELTABLE (TAKIONID, TOTAL_DELTA, QUANTITY) VALUES (?,?,?)''', (TKID[i], total_d[i], qty[i] ))
    print("checkpoint 3****")
    cur.execute('''UPDATE EXCELTABLE SET (PolicyNumber,CarryForwardBalance,StartingBalance) = (SELECT gemscap_table.PolicyNumber, gemscap_table.CarryForwardBalance,gemscap_table.StartingBalance
                FROM gemscap_table WHERE gemscap_table.TakionID = EXCELTABLE.TAKIONID)''')
    print("checkpoint 4****")
    
    cur.execute('''SELECT TAKIONID, TOTAL_DELTA, PolicyNumber , CarryForwardBalance, NetPay, StartingBalance FROM EXCELTABLE ''')
    print("checkpoint 5****")
    row = cur.fetchone()
    global payable
    while(row):
        print("row is :",row)
        if row[1]=='' or row[1]==None or row[3]==None:
            row = cur.fetchone()
            continue
        if row[1] >= 0 and row[3] >= 0:   #if td and cfb is positive                                          
                                                                           
            if row[2] == 1:
                payable.append(round(row[1]*0.85,2))
            elif row[2] == 0:
                payable.append(round(row[1]*0.70,2))
            #else:payable.append(-1)
        elif row[1] < 0 and row[3] >= 0:    # if td is -ve and cfb is +ve
            payable.append(round(row[1],2))

        
######################################################      30  SEP
        elif (row[1] < 0 and row[3] < 0):  ##   -ve -ve
            if abs(row[3]) >= 0.80*(row[5]):
                print("defaulter: ",row[0])
                defaulterstr = defaulterstr + str(row[0]) + " "
            payable.append(round(row[1],2))


        ##also check for defaulter in this case
        elif (row[1] > 0 and row[3] < 0):        # if td is +ve and cfb is -

            if abs(row[3]) >= 0.80*(row[5]):
                print("defaulter: ",row[0])
                defaulterstr = defaulterstr + str(row[0]) + " "

            if(row[1] < abs(row[3])):
                payable.append(round(row[1],2))     ##append 100% eg cfb = -300 td = 100
                
            elif(row[1] > abs(row[3])):             ## eg cfb = -300 td = 600  i.e 300 + 300*policy 
                if(row[2]==1):
                    res = abs(row[3]) + (row[1] - abs(row[3]))*0.85
                    payable.append(round(res , 2))
                elif(row[2]==0):
                    abs(row[3]) + (row[1] - abs(row[3]))*0.70
                    payable.append(round(res , 2))
        
        
        
        row = cur.fetchone()
    
    print(payable)
    print("LENGTH OF PAYABLE :",len(payable))
    con.commit()
    con.close()
    return defaulterstr

#######################################################################################################

def updatenetpay():
    print("INSIDE CREATE updatenetpay()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    global TKID
    global payable
    print(TKID)
    for i in range(len(TKID)):
        x=TKID[i]
        print(x)
        #script='INSERT INTO EXCELTABLE (NetPay) VALUES (?) WHERE TAKIONID=7090100' , (payable[i])
        curs.execute('UPDATE EXCELTABLE SET NetPay = {}  WHERE TAKIONID= {}'.format(payable[i], TKID[i])  )
        #curs.execute('INSERT INTO EXCELTABLE (NetPay) VALUES (?) WHERE TAKIONID={}'.format(TKID[i]), (payable[i],) )
    conn.commit()
    conn.close()

#######################################################################################################

def updateCarryForwardBalance():
    print("INSIDE  updateCarryForwardBalance()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    global TKID
    for i in range(len(TKID)):
        curs.execute('UPDATE EXCELTABLE SET CarryForwardBalance = CarryForwardBalance + NetPay  WHERE TAKIONID= {}'.format(TKID[i])  )
    conn.commit()
    conn.close()

#######################################################################################################

def updateCarryForwardBalanceInGemscap():
    print("INSIDE  updateCarryForwardBalanceInGemscap()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    #curs.execute('UPDATE gemscap_table SET CarryForwardBalance = EXCELTABLE.CarryForwardBalance FROM EXCELTABLE WHERE TakionID= EXCELTABLE.TAKIONID')
    curs.execute('''UPDATE gemscap_table
SET
      CarryForwardBalance = (SELECT EXCELTABLE.CarryForwardBalance 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID )
WHERE
    EXISTS (
        SELECT *
        FROM EXCELTABLE
        WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID
    )
''')
    conn.commit()
    conn.close()

#######################################################################################################

def updatetotalInGemscap():
    print("INSIDE  updatetotalInGemscap()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    #curs.execute('UPDATE gemscap_table SET CarryForwardBalance = EXCELTABLE.CarryForwardBalance FROM EXCELTABLE WHERE TakionID= EXCELTABLE.TAKIONID')
    curs.execute('''UPDATE gemscap_table
                    SET
                    Total = Total + (SELECT EXCELTABLE.TOTAL_DELTA 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID )
                    WHERE
                        EXISTS (
                            SELECT *
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID
                        )''')

    conn.commit()
    conn.close()

#######################################################################################################

def updatequantity():
    print("INSIDE  updatequantity()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute('''UPDATE gemscap_table
    SET
      Qty = Qty + (SELECT EXCELTABLE.QUANTITY 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID )
    WHERE
        EXISTS (
            SELECT *
            FROM EXCELTABLE
            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID
        )
''')
    conn.commit()
    conn.close()

#######################################################################################################

def cleardata():
    print("INSIDE CREATE cleardata()")
    global TKID
    TKID.clear()
    global total_d
    total_d.clear()
    global payable
    payable.clear()
    global qty
    qty.clear()

##############################################PAID#################################

def printpayabledata(x):
    print("INSIDE printpayabledatabledata()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute('''SELECT * FROM gemscap_table WHERE TakionID = {}'''.format(x))
    row = curs.fetchall()
    #print(row)
    print(row[0][49])
    conn.commit()
    conn.close()
    return row[0][49]

#######################################################################################################

def deductamount(x,y):
    print("INSIDE Deductamount")
    print('takionid = ',x, 'amount = ',y)
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute('''UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance - {} WHERE TakionID = {}'''.format(float(y),x))
    conn.commit()
    conn.close()
    
#######################################################################################################

#################################     24 oct     ##############################
def calculateage(eid):                     ## works for tuype dd/mm/yyyy in database else fails
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute("SELECT DOB from gemscap_table WHERE EmployeeID = '" + str(eid) + "'")
    BirthDate = curs.fetchone()
    #print(BirthDate[0])
    born = BirthDate[0]
    conn.commit()
    conn.close()

    born = born.split("/")
    day=int(born[0])
    month=int(born[1])
    year=int(born[2])
    born=(date(year,month,day))
    print(born,"datetype data")

    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
  
    # raised when birth date is February 29 
    # and the current year is not a leap year 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year
    
# openfile('sasample2')
# createexceltable()
# updatequantity()