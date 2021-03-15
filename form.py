from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, validators, ValidationError,SelectField
from wtforms.fields.html5 import EmailField

class userform(FlaskForm):
    ID1 = SelectField('ID1 ' , choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')] ,validators = [validators.DataRequired()])
    ID2 = SelectField('ID2' ,choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')], validators = [validators.DataRequired()])
    ID3 = SelectField('ID3',choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    ID4 = SelectField('ID4' , choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID5 = SelectField('ID5' ,choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')], validators = [validators.DataRequired()])
    ID6 = SelectField('ID6' , choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])

    ID7 = SelectField('ID7', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID8 = SelectField('ID8' ,choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID9 = SelectField('ID9', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    ID10 = SelectField('ID10' , choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID11 = SelectField('ID11', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID12 = SelectField('ID12', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID13 = SelectField('ID13', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID14 = SelectField('ID14' , choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators=[validators.DataRequired()])
    ID15 = SelectField('ID15', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID16 = SelectField('ID16', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])
    ID17 = SelectField('ID17', choices=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')],validators = [validators.DataRequired()])

    submit = SubmitField('Submit')

class printdata(FlaskForm):
    EmployeeAccNo = StringField('ENTER EMPLOYEE\'S GEMSCAP ID')

class printdeldata(FlaskForm):
    EmployeeAccNo = StringField('ENTER EMPLOYEE\'S GEMSCAP ID')

class updateExcel(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    Excel = StringField('FILE NAME')

class paidDetails(FlaskForm):
    Paid = StringField('TAKION ID')

class amountToPay(FlaskForm):
    Paida = StringField('RE-ENTER TAKION ID')
    PaidAmount = StringField('ENTER AMOUNT TO PAY')

class payToIndividual(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    PayAmount = StringField('AMOUNT TO PAY')
    submit1 = SubmitField('Submit')

class indiMonthlyView(FlaskForm):
    TakionId = StringField('TAKION ID')

class indiPayView(FlaskForm):
    TakionId = StringField('TAKION ID')

class adjustform(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    Takionid = StringField('TAKION ID')
    Amount = StringField('AMOUNT TO ADJUST')
    submit = SubmitField('Submit')

class updatekyc(FlaskForm):
    TakionID = StringField('Takion ID', validators = [validators.DataRequired()])
    PolicyNumber = RadioField('PolicyNumber', choices = [('0','70%'), ('1','85%')], validators = [validators.DataRequired()])
    ContactNumber2 = StringField('Contact Number 2',validators = [validators.DataRequired(), validators.Regexp(regex = r'^(\+91){1}[1-9]{1}[0-9]{9}$', message = "MOBILE NO STARTING WITH +91")])
    MaritialStatus = RadioField('Maritial Status', choices = [('M','Married'),('U','Unmarried'),('O','Other') ] )
    LocalAddress = StringField('Local Address' , validators=[validators.DataRequired()])
    City2 = StringField('City', validators = [validators.DataRequired()])
    Pincode2 = StringField('Pin Code', validators = [validators.DataRequired()])
    Country2 = StringField('Country', validators = [validators.DataRequired()])
    #PolicyNumber = RadioField('PolicyNumber', choices = [('0','70%'), ('1','85%')], validators = [validators.DataRequired()])
    PFNomineeName = StringField('PF Nominee Name', validators = [validators.DataRequired()])
    PFNomineeRelation = StringField('PF Nominee Relation', validators = [validators.DataRequired()])
    PFNomineeDOB = StringField('PF Nominee DOB', validators = [validators.DataRequired()])
    DateOfResigning = StringField('Date Of Resigning')
    AccountNumber2 = StringField('Account Number 2', [validators.Regexp(regex = r'^[0-9]{9,18}$', message="")])
    IFSCcode2 = StringField('IFSC Code')
    BankName2 = StringField('Bank Name')
    AccountType2 = StringField('Account Type') 
    AccountHolderName2 = StringField('Account Holder Name')
    submit = SubmitField('Submit')

class deleteform(FlaskForm):
    TakionID = StringField('TAKION ID', validators = [validators.DataRequired()])
    submit = SubmitField('Submit')

class adjustpaymentform(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    Takionid = StringField('TAKION ID')
    Amount = StringField('AMOUNT TO ADJUST')
    submit = SubmitField('Submit')


class submit(FlaskForm):
    submit = SubmitField('Submit')